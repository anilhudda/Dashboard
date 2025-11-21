from __future__ import annotations

import logging
import threading
from typing import Sequence

from app.clients.base import BrokerClient
from app.models.account_snapshot import AccountSnapshot
from app.services.data_store import DataStore

logger = logging.getLogger(__name__)


class Aggregator:
    """Pulls metrics from all broker clients on a schedule."""

    def __init__(
        self,
        clients: Sequence[BrokerClient],
        store: DataStore,
        refresh_seconds: int = 60,
    ) -> None:
        self._clients = clients
        self._store = store
        self._refresh_seconds = refresh_seconds
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

    def refresh_once(self) -> None:
        for client in self._clients:
            try:
                snapshot: AccountSnapshot = client.fetch_account_snapshot()
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.exception("Failed to fetch snapshot for broker %s: %s", client.name, exc)
                continue
            self._store.update_snapshot(snapshot)
            logger.debug("Updated snapshot for broker %s", client.name)

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, name="AggregatorLoop", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=self._refresh_seconds)

    def _run_loop(self) -> None:
        logger.info("Aggregator loop started with %s-second cadence", self._refresh_seconds)
        self.refresh_once()
        while not self._stop_event.wait(self._refresh_seconds):
            self.refresh_once()
        logger.info("Aggregator loop stopped")


__all__ = ["Aggregator"]
