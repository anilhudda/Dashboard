from __future__ import annotations

from abc import ABC, abstractmethod

from app.models.account_snapshot import AccountSnapshot


class BrokerClient(ABC):
    """Abstract client that knows how to talk to a broker API."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def fetch_account_snapshot(self) -> AccountSnapshot:
        """Return the latest account metrics for this broker."""


__all__ = ["BrokerClient"]
