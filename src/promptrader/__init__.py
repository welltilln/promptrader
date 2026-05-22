"""promptrader — LLM-driven trading agent framework.

See VISION.md and SCOPE.md for project goals.
"""

__version__ = "0.0.1"

from .agent import LLMTrader, ModelCallable
from .risk import Risk
from . import brokers, prompts

__all__ = ["LLMTrader", "ModelCallable", "Risk", "brokers", "prompts"]
