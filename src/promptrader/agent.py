"""LLMTrader — the agent loop.

Connects a prompt template, an LLM model, a broker, and risk guardrails.
"""

from dataclasses import dataclass, field
from typing import Any, Callable

from .brokers.base import Broker, Order
from .prompts.base import Prompt, Decision
from .risk import Risk


# Type for a "model callable" — takes (system, user) returns text.
# Lets us swap Anthropic/OpenAI/Ollama without coupling to any SDK.
ModelCallable = Callable[[str, str], str]


@dataclass
class LLMTrader:
    model: ModelCallable
    broker: Broker
    prompt: Prompt
    risk: Risk = field(default_factory=Risk)

    _starting_equity: float | None = None
    _tokens_spent_usd: float = 0.0
    _halted: bool = False

    def step(self, context: dict[str, Any]) -> Decision | None:
        """Run one decision cycle. Returns the Decision taken, or None if halted."""
        if self._halted:
            return None

        equity = self.broker.get_equity()
        if self._starting_equity is None:
            self._starting_equity = equity

        if self.risk.check_drawdown(equity, self._starting_equity):
            self._halted = True
            return None
        if self.risk.check_token_budget(self._tokens_spent_usd):
            self._halted = True
            return None

        sys_msg = self.prompt.system_message()
        usr_msg = self.prompt.user_message(context)
        response = self.model(sys_msg, usr_msg)
        decision = self.prompt.parse(response)

        if self.risk.kill_switch:
            return decision  # observed but not executed

        if decision.action == "hold":
            return decision

        size = max(0.0, min(decision.size, 1.0)) * self.risk.max_position_size
        volume = size * equity / max(context.get("price", 1.0), 1e-9)
        if self.risk.check_position_size(volume * context.get("price", 0.0), equity):
            return decision  # rejected

        self.broker.submit(Order(
            symbol=decision.symbol,
            side="buy" if decision.action == "buy" else "sell",
            volume=volume,
        ))
        return decision

    @property
    def halted(self) -> bool:
        return self._halted
