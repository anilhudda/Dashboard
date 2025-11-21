from __future__ import annotations

import atexit
import logging
from app.app_factory import create_dashboard_app
from app.clients.mock import MockTradingClient
from app.utils.settings import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
clients = [
    MockTradingClient("Jainam", seed=1),
    MockTradingClient("Zerodha", seed=2),
    MockTradingClient("Mastertrust", seed=3),
]

app, aggregator, store = create_dashboard_app(
    clients=clients,
    refresh_seconds=settings.refresh_seconds,
    start_scheduler=True,
)


def _stop_background_services() -> None:
    aggregator.stop()


atexit.register(_stop_background_services)
server = app.server


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
