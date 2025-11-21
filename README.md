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

## Testing
- `pytest` runs the full suite (unit, integration, and Dash/Selenium end-to-end coverage).
- End-to-end tests require Google Chrome (or Chromium) and a matching `chromedriver` binary on your `PATH`.
  - Linux quick start:
    ```bash
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install -y ./google-chrome-stable_current_amd64.deb
    CHROMEDRIVER_PATH="$(python - <<'PY'
    from webdriver_manager.chrome import ChromeDriverManager
    print(ChromeDriverManager().install())
    PY
    )"
    sudo cp "$CHROMEDRIVER_PATH" /usr/local/bin/chromedriver
    sudo chmod +x /usr/local/bin/chromedriver
    ```
- The suite uses mock broker clients, so no external APIs are called during CI.

## Docker
Build and run a portable container:
```bash
docker build -t broker-dashboard .
docker run --env-file .env -p 8050:8050 broker-dashboard
```

## Continuous Integration & Deployment
- `.github/workflows/ci.yml` executes on every push/PR against `main`.
  - Installs Chrome + Chromedriver, then runs `pytest --cov=app`.
  - On pushes to `main`, it builds the Docker image and publishes it to `ghcr.io/<org>/<repo>:{latest,sha}` using the built-in `GITHUB_TOKEN`.
- To pull the published image elsewhere:
  ```bash
  docker pull ghcr.io/<org>/<repo>:latest
  docker run --env-file .env -p 8050:8050 ghcr.io/<org>/<repo>:latest
  ```