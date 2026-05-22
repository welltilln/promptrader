# promptrader

**A Python framework for LLM-driven trading agents.**

```bash
pip install promptrader   # coming soon
```

```python
import promptrader as pt

agent = pt.LLMTrader(
    model="claude-opus-4-7",
    broker=pt.brokers.Nautilus(...),
    risk=pt.Risk(max_drawdown=0.05),
    prompt=pt.prompts.NewsSentiment(symbols=["AAPL", "BTC-USD"]),
)
agent.backtest(start="2025-01-01", end="2025-12-31")
agent.run_live()
```

## Why

LLMs can reason about markets (news, earnings, macro narratives). Python already connects to most brokers (Nautilus, ccxt, ib_insync, MetaTrader5). The missing layer: a clean framework for **putting LLMs in the loop** — with prompt templates, cost controls, risk guards, and (crucially) **a way to backtest without burning tokens**.

## What It Is

- **Pure Python** — no Rust, no compile step
- **Broker-agnostic** — delegates execution to Nautilus / ccxt / MT5
- **LLM-agnostic** — Anthropic, OpenAI, local Ollama, all equal
- **MIT licensed** — open source, no strings

## What It Is NOT

- Not a matching engine — Nautilus does that
- Not a charting platform — TradingView does that
- Not an HFT system — wrong layer
- Not a MetaTrader replacement — wrong battle

See `VISION.md` and `SCOPE.md` for details.

## Status

Pre-alpha. Side project. Not yet on PyPI. Not yet on GitHub publicly.

## License

MIT (planned at v0.1.0 publish).
