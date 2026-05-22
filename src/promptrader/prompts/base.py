"""Base prompt + LLM decision contract.

A Prompt knows:
  - What system message to give the model
  - What user message to render given current market context

The model returns a Decision: action (buy/sell/hold), symbol, size, reasoning.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal


Action = Literal["buy", "sell", "hold"]


@dataclass
class Decision:
    action: Action
    symbol: str
    size: float = 0.0  # fraction of allowed position size (0–1)
    reasoning: str = ""
    raw_response: str = ""


class Prompt(ABC):
    """A reusable prompt template for an LLM trading agent."""

    @abstractmethod
    def system_message(self) -> str:
        """Persistent instruction given to the model."""

    @abstractmethod
    def user_message(self, context: dict[str, Any]) -> str:
        """Per-tick prompt given current market context (price, news, etc.)."""

    @abstractmethod
    def parse(self, model_response: str) -> Decision:
        """Parse the model's reply into a structured Decision."""
