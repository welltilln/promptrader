# promptrader: LLM Trading Agent Framework

**A Python framework for building LLM-driven trading agents that connect to real brokers via existing infrastructure.**

---

## 1. The Problem
Two real shifts are happening in 2026:

1. **LLMs can reason about markets** — news, earnings, macro narratives, sentiment. Hedge funds already use them. Retail traders cannot, easily.

2. **Python connects to most brokers now** — through Nautilus, ccxt, ib_insync, the official MetaTrader5 package. The plumbing exists.

What's missing is the **layer in between**:
- How do I let an LLM decide trades?
- How do I structure prompts for market context?
- How do I rate-limit, cost-control, and risk-guard an agent?
- How do I backtest an LLM strategy without spending $10k on tokens?

promptrader fills this gap.

## 2. What promptrader Is
A pure-Python library that lets you write LLM-driven trading agents in ~20 lines of code, regardless of broker:

```python
import promptrader as pt

agent = pt.LLMTrader(
    model="claude-opus-4-7",
    broker=pt.brokers.Nautilus(...),    # or ccxt, MT5, IBKR
    risk=pt.Risk(max_drawdown=0.05),
    prompt=pt.prompts.NewsSentiment(symbols=["AAPL", "BTC-USD"]),
)
agent.backtest(start="2025-01-01", end="2025-12-31")
agent.run_live()
```

## 3. What promptrader Is NOT
- ❌ A matching engine — Nautilus, ccxt, MT5 do this.
- ❌ A broker terminal/GUI — TradingView, MT5, brokers' apps do this.
- ❌ A backtest engine from scratch — Nautilus, Backtrader, Vectorbt do this.
- ❌ A high-frequency platform — wrong layer for HFT.
- ❌ A replacement for MetaTrader — wrong battle.

promptrader is **the LLM strategy layer**. Everything else, we delegate.

## 4. Target User
**The Python-fluent trader/quant who wants to put AI in their strategy** but doesn't want to:
- Glue OpenAI/Anthropic SDK to a broker by hand
- Reinvent prompt templates for market data
- Build cost controls / rate limits / retry logic
- Figure out how to backtest LLM strategies (the hard part)

Not for: beginners who can't write Python. Not for: HFT firms. Not for: people happy with manual MT5 trading.

## 5. The Wedge
**Backtesting LLM strategies without burning tokens.**

No one has solved this well. Naive replay = $$$$ in API costs. promptrader's value: cached LLM responses + deterministic replay + prompt versioning, so you can backtest a year of strategy for the cost of one month of API calls.

If we ship this one thing well, we have a defensible reason to exist.

## 6. Anti-Goals
- Multi-language support (Python only, forever)
- Custom Rust core, custom matching engine (delegate)
- Mobile app, desktop GUI, web terminal
- Crypto-only or stocks-only specialization
- LLM provider lock-in (support Anthropic, OpenAI, local Ollama equally)

## 7. License & Distribution
- **MIT License** — open source, no monetization for first 12-18 months.
- **`pip install promptrader`** — pure Python, no Rust/build complexity.
- **Side project** — maintainer has day job; no VC, no runway pressure.

## 8. Success Signals (12-18 months)
- 1+ non-maintainer user opens a real issue
- Featured in Anthropic / OpenAI cookbook or one financial Python blog
- GitHub stars from accounts that look like real traders/quants
- At least 1 external PR

If none of these by month 18 → reconsider. No sunk-cost continuation.

---
**Status:** Pre-alpha
**License:** MIT
**Maintainer:** welltilln (side project)
**Predecessor:** This project replaces `pytrdr` (Rust core, over-scoped). See `pytrdr/` archive for prior exploration.
