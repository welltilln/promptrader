"""Base broker interface — implemented by ccxt, nautilus, MT5 adapters."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal


Side = Literal["buy", "sell"]


@dataclass
class Order:
    symbol: str
    side: Side
    volume: float
    price: float | None = None  # None = market order


@dataclass
class Position:
    symbol: str
    side: Side
    volume: float
    entry_price: float
    current_price: float

    @property
    def unrealized_pnl(self) -> float:
        diff = self.current_price - self.entry_price
        if self.side == "sell":
            diff = -diff
        return diff * self.volume


class Broker(ABC):
    """Abstract broker. Subclass for ccxt / nautilus / MT5."""

    @abstractmethod
    def get_equity(self) -> float:
        """Return current account equity in account currency."""

    @abstractmethod
    def get_positions(self) -> list[Position]:
        """Return all open positions."""

    @abstractmethod
    def submit(self, order: Order) -> str:
        """Submit an order. Return broker order id."""

    @abstractmethod
    def close(self, symbol: str) -> None:
        """Close all positions for a symbol."""
