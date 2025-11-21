from __future__ import annotations

from collections import defaultdict, deque
from threading import Lock
from typing import Deque, Dict, Iterable

from app.models.account_snapshot import AccountSnapshot


class DataStore:
    """Thread-safe in-memory store for broker snapshots and history."""

    def __init__(self, history_limit: int = 720):
        self._lock = Lock()
        self._history_limit = history_limit
        self._latest: Dict[str, AccountSnapshot] = {}
        self._history: Dict[str, Deque[AccountSnapshot]] = defaultdict(lambda: deque(maxlen=self._history_limit))

    def update_snapshot(self, snapshot: AccountSnapshot) -> None:
        with self._lock:
            self._latest[snapshot.broker] = snapshot
            self._history[snapshot.broker].append(snapshot)

    def get_latest(self) -> Dict[str, AccountSnapshot]:
        with self._lock:
            return {broker: snapshot.model_copy(deep=True) for broker, snapshot in self._latest.items()}

    def get_history(self, broker: str) -> Iterable[AccountSnapshot]:
        with self._lock:
            history = list(self._history.get(broker, []))
        return history

    def brokers(self) -> list[str]:
        with self._lock:
            return list(self._latest.keys())


__all__ = ["DataStore"]
