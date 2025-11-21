from __future__ import annotations

import pytest

from app.app_factory import create_dashboard_app


@pytest.mark.e2e
def test_dashboard_displays_cards(dash_duo, mock_clients):
    app, aggregator, store = create_dashboard_app(
        clients=mock_clients,
        refresh_seconds=1,
        start_scheduler=False,
    )

    aggregator.refresh_once()

    dash_duo.start_server(app)

    dash_duo.wait_for_element("#last-updated", timeout=10)
    dash_duo.wait_for_text_to_equal("h1.app-title", "Multi-Broker Trading Dashboard", timeout=10)

    cards = dash_duo.find_elements(".summary-card")
    assert len(cards) == len(mock_clients)
