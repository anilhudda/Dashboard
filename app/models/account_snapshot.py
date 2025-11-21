from __future__ import annotations

from datetime import datetime
from typing import Any, List

from pydantic import BaseModel, Field


class Position(BaseModel):
    symbol: str
    quantity: float
    pnl: float | None = None
    meta: dict[str, Any] = Field(default_factory=dict)


class AccountSnapshot(BaseModel):
    broker: str
    timestamp: datetime
    pnl: float
    net_margin: float
    available_margin: float
    order_count: int
    open_positions: List[Position] = Field(default_factory=list)
    raw: dict[str, Any] = Field(default_factory=dict)
