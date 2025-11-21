from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    refresh_seconds: int = int(os.getenv("REFRESH_SECONDS", "60"))
    jainam_api_key: str = os.getenv("JAINAM_API_KEY", "")
    zerodha_api_key: str = os.getenv("ZERODHA_API_KEY", "")
    mastertrust_api_key: str = os.getenv("MASTERTRUST_API_KEY", "")


settings = Settings()


__all__ = ["settings", "Settings"]
