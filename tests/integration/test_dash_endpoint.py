from __future__ import annotations

from app.app_factory import create_dashboard_app


def test_dash_homepage_returns_200(mock_clients):
    app, aggregator, store = create_dashboard_app(
        clients=mock_clients,
        refresh_seconds=1,
        start_scheduler=False,
    )

    aggregator.refresh_once()

    client = app.server.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Broker PnL Monitor" in response.data
