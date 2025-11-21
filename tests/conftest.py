from __future__ import annotations

import os

import pytest
from selenium.webdriver.chrome.options import Options

from app.clients.mock import MockTradingClient

os.environ.setdefault("CHROME_BIN", "/usr/bin/google-chrome-stable")
os.environ.setdefault("DASH_TESTING_WAIT_TIMEOUT", "10")


def pytest_setup_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.binary_location = os.environ.get("CHROME_BIN")
    return options


@pytest.fixture
def mock_clients():
    """Provide deterministic clients for tests."""

    return [
        MockTradingClient("JainamTest", seed=11),
        MockTradingClient("ZerodhaTest", seed=22),
        MockTradingClient("MastertrustTest", seed=33),
    ]
