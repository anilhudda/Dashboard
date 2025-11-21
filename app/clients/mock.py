from __future__ import annotations

import random
from datetime import datetime, timedelta
from typing import Sequence

from app.clients.base import BrokerClient
from app.models.account_snapshot import AccountSnapshot, Position


class MockTradingClient(BrokerClient):
    """Simple mock that fabricates metrics. Replace with real clients in production."""

    def __init__(self, name: str, seed: int | None = None):
        super().__init__(name)
        self._rng = random.Random(seed)
        # start with a pseudo-random pnl baseline so cards look distinct
        self._pnl = self._rng.uniform(-5000, 5000)

    def fetch_account_snapshot(self) -> AccountSnapshot:
        pnl_delta = self._rng.uniform(-250, 250)
        self._pnl += pnl_delta
        net_margin = self._rng.uniform(50000, 150000)
        available_margin = net_margin - self._rng.uniform(5000, 20000)
        order_count = self._rng.randint(5, 35)
        open_positions = self._build_positions(self._rng.randint(1, 5))

        return AccountSnapshot(
            broker=self.name,
            timestamp=datetime.utcnow(),
            pnl=round(self._pnl, 2),
            net_margin=round(net_margin, 2),
            available_margin=round(available_margin, 2),
            order_count=order_count,
            open_positions=open_positions,
            raw={"note": "mock data"},
        )

    def _build_positions(self, count: int) -> Sequence[Position]:
        symbols = ["NIFTY", "BANKNIFTY", "RELIANCE", "TATASTEEL", "HDFCBANK"]
        positions: list[Position] = []
        base_time = datetime.utcnow()
        for _ in range(count):
            symbol = self._rng.choice(symbols)
            quantity = self._rng.choice([25, 50, 75, 100])
            pnl = round(self._rng.uniform(-1500, 1500), 2)
            positions.append(
                Position(
                    symbol=symbol,
                    quantity=quantity,
                    pnl=pnl,
                    meta={"opened": (base_time - timedelta(minutes=self._rng.randint(1, 120))).isoformat()},
                )
            )
        return positions


__all__ = ["MockTradingClient"]
