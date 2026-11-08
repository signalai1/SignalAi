# Signal AI

Signal AI is a web-based market research interface starter.

## Deploy on Render
1. Push the contents of this folder to a GitHub repository named `signal-ai`.
2. In Render, choose **New + → Blueprint** and connect the repository.
3. Render reads `render.yaml` and builds the Flask service.

## Current scope
- Home page with searchable sample commodity and crypto market lists.
- Separate Charts view with selectable 1m, 5m and 15m display intervals.
- Heikin-Ashi display preference in the interface.
- Health endpoint at `/health`.

## Important
This starter does **not** connect to live Kalshi quotes, TradingView market feeds, or place trades. Market names in the list are a navigation/catalog starter, not live contracts or recommendations. Do not use it to make real-money decisions. A verified data provider and signal logic must be integrated and tested before live use.
