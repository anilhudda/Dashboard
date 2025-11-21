from __future__ import annotations

from datetime import datetime, timedelta

from app.models.account_snapshot import AccountSnapshot, Position
from app.services.data_store import DataStore


def make_snapshot(broker: str, pnl: float, timestamp: datetime | None = None) -> AccountSnapshot:
    ts = timestamp or datetime.utcnow()
    return AccountSnapshot(
        broker=broker,
        timestamp=ts,
        pnl=pnl,
        net_margin=100000.0,
        available_margin=75000.0,
        order_count=5,
        open_positions=[
            Position(symbol="NIFTY", quantity=50, pnl=pnl / 2),
        ],
    )


def test_data_store_tracks_latest_and_history():
    store = DataStore(history_limit=2)
    snap1 = make_snapshot("BrokerA", 100.0, datetime.utcnow() - timedelta(minutes=1))
    snap2 = make_snapshot("BrokerA", 150.0)

    store.update_snapshot(snap1)
    store.update_snapshot(snap2)

    latest = store.get_latest()
    assert "BrokerA" in latest
    assert latest["BrokerA"].pnl == 150.0

    history = list(store.get_history("BrokerA"))
    assert len(history) == 2
    assert history[0].pnl == 100.0
    assert history[1].pnl == 150.0
