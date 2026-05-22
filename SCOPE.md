# promptrader: Scope

## In Scope (v0.1.0 target)
1. **`LLMTrader` class** — agent loop with model/broker/risk/prompt config
2. **Broker adapters** (thin wrappers, not reimplementations):
   - Nautilus (priority 1 — covers IBKR, Binance, Bybit, etc.)
   - ccxt (priority 2 — crypto exchanges)
   - Optional later: official `MetaTrader5` pip package
3. **Prompt templates library**:
   - `NewsSentiment`, `EarningsReaction`, `MacroNarrative`, `TechnicalReasoning`
4. **Backtest engine**:
   - LLM response cache (the wedge)
   - Replay over historical data using cached responses
   - Cost estimator before running
5. **Risk module**:
   - Max drawdown, position size limits, kill switch
   - Per-call cost cap (token budget)
6. **Examples** (3-5 working notebooks):
   - News-driven crypto agent (ccxt)
   - Earnings-trade equity agent (Nautilus + IBKR)
   - Macro narrative FX agent

## Out of Scope (forever, or until v1.0)
- Custom matching/order book
- Custom GUI / chart renderer
- FIX gateway / direct LP connectivity
- HFT execution
- Strategy marketplace
- ZKP / signal IP protection
- Multi-language SDK
- White-label broker offering

## Deferred (revisit at v0.5)
- WebUI for monitoring agents (Streamlit/Gradio plugin, not custom)
- Hosted/cloud version (only if usage demands)
- Premium prompt templates
