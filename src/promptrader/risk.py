"""Risk module — guards an LLM agent from runaway losses or runaway tokens."""

from dataclasses import dataclass


@dataclass
class Risk:
    """Risk guardrails for an LLMTrader.

    Attributes
    ----------
    max_drawdown:
        Fraction of starting equity at which the agent halts. e.g. 0.05 = 5%.
    max_position_size:
        Max position size as fraction of equity per trade. e.g. 0.1 = 10%.
    token_budget_usd:
        Hard cap on LLM API spend per run, in USD. None = uncapped.
    kill_switch:
        If True, suspend new orders but keep monitoring existing positions.
    """

    max_drawdown: float = 0.10
    max_position_size: float = 0.10
    token_budget_usd: float | None = None
    kill_switch: bool = False

    def check_drawdown(self, current_equity: float, starting_equity: float) -> bool:
        """Return True if drawdown limit has been hit."""
        if starting_equity <= 0:
            return False
        dd = (starting_equity - current_equity) / starting_equity
        return dd >= self.max_drawdown

    def check_position_size(self, position_value: float, equity: float) -> bool:
        """Return True if position would exceed size limit."""
        if equity <= 0:
            return True
        return (position_value / equity) > self.max_position_size

    def check_token_budget(self, spent_usd: float) -> bool:
        """Return True if token budget has been exceeded."""
        if self.token_budget_usd is None:
            return False
        return spent_usd >= self.token_budget_usd
