from __future__ import annotations

from app.services.aggregator import Aggregator
from app.services.data_store import DataStore


def test_aggregator_refreshes_all_clients(mock_clients):
    store = DataStore(history_limit=10)
    aggregator = Aggregator(clients=mock_clients, store=store, refresh_seconds=1)

    aggregator.refresh_once()

    latest = store.get_latest()
    assert len(latest) == len(mock_clients)
    assert all(broker in latest for broker in ("JainamTest", "ZerodhaTest", "MastertrustTest"))
