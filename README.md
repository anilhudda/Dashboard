# Multi-Broker Trading Dashboard

Dash-based control panel that aggregates PnL, margin, order, and position metrics
from Jainam, Zerodha, and Mastertrust trading accounts.

## Features
- Background aggregator that pulls metrics from every configured broker every 60 seconds
- Thread-safe in-memory store that holds the latest snapshot plus a rolling history per broker
- Plotly Dash UI with summary cards, PnL history chart, and consolidated positions table
- .env-driven configuration so you can plug in production API keys without changing code

## Prerequisites
- Python 3.11+
- Access credentials for Jainam, Zerodha, and Mastertrust APIs

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your API keys + preferred refresh cadence
```

## Running the dashboard
```bash
python -m app.main
```
Open http://localhost:8050 to view the dashboard.

The app ships with mock clients so you can see the UI immediately. Replace the
`MockTradingClient` instances in `app/main.py` with your real API wrappers that
implement `BrokerClient.fetch_account_snapshot()`. Each call should return an
`AccountSnapshot` populated with PnL, margins, order counts, and open positions.