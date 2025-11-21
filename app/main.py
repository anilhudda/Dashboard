from __future__ import annotations

import atexit
import logging
from datetime import datetime
from typing import Dict, List

import pandas as pd
from dash import Dash, Input, Output, dash_table, dcc, html
import plotly.graph_objects as go

from app.clients.mock import MockTradingClient
from app.models.account_snapshot import AccountSnapshot
from app.services.aggregator import Aggregator
from app.services.data_store import DataStore
from app.utils.settings import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

store = DataStore(history_limit=1440)
clients = [
    MockTradingClient("Jainam", seed=1),
    MockTradingClient("Zerodha", seed=2),
    MockTradingClient("Mastertrust", seed=3),
]

aggregator = Aggregator(clients=clients, store=store, refresh_seconds=settings.refresh_seconds)


def _start_background_services() -> None:
    try:
        aggregator.start()
    except Exception as exc:  # pragma: no cover - startup guard
        logger.exception("Failed to start aggregator: %s", exc)


def _stop_background_services() -> None:
    aggregator.stop()


_start_background_services()
atexit.register(_stop_background_services)


def make_dash_app() -> Dash:
    app = Dash(__name__)
    app.title = "Broker PnL Monitor"

    app.layout = html.Div(
        [
            html.H1("Multi-Broker Trading Dashboard", className="app-title"),
            html.Div(id="last-updated", className="last-updated"),
            dcc.Interval(id="data-refresh", interval=settings.refresh_seconds * 1000, n_intervals=0),
            html.Div(id="broker-cards", className="cards-grid"),
            dcc.Graph(id="pnl-history"),
            html.H2("Open Positions", className="section-title"),
            dash_table.DataTable(
                id="positions-table",
                columns=[
                    {"name": "Broker", "id": "broker"},
                    {"name": "Symbol", "id": "symbol"},
                    {"name": "Quantity", "id": "quantity"},
                    {"name": "PnL", "id": "pnl", "type": "numeric", "format": {"specifier": ".2f"}},
                ],
                data=[],
                style_table={"maxHeight": "400px", "overflowY": "auto"},
                style_cell={"textAlign": "center"},
            ),
        ],
        className="app-container",
    )

    @app.callback(
        Output("broker-cards", "children"),
        Output("positions-table", "data"),
        Output("pnl-history", "figure"),
        Output("last-updated", "children"),
        Input("data-refresh", "n_intervals"),
    )
    def refresh_dashboard(_):
        snapshots = store.get_latest()
        cards = _build_cards(snapshots)
        positions = _build_positions_table(snapshots)
        figure = _build_pnl_history()
        last_updated = _format_last_updated(snapshots)
        return cards, positions, figure, last_updated

    return app


def _build_cards(snapshots: Dict[str, AccountSnapshot]):
    cards: List[html.Div] = []
    for name, snapshot in sorted(snapshots.items()):
        cards.append(
            html.Div(
                [
                    html.H3(name, className="card-title"),
                    html.Div([
                        html.Span("PnL"),
                        html.Strong(f"₹ {snapshot.pnl:,.2f}"),
                    ], className="card-row"),
                    html.Div([
                        html.Span("Net Margin"),
                        html.Strong(f"₹ {snapshot.net_margin:,.2f}"),
                    ], className="card-row"),
                    html.Div([
                        html.Span("Available Margin"),
                        html.Strong(f"₹ {snapshot.available_margin:,.2f}"),
                    ], className="card-row"),
                    html.Div([
                        html.Span("Orders"),
                        html.Strong(str(snapshot.order_count)),
                    ], className="card-row"),
                    html.Div([
                        html.Span("Open Positions"),
                        html.Strong(str(len(snapshot.open_positions))),
                    ], className="card-row"),
                ],
                className="summary-card",
            )
        )
    if not cards:
        cards.append(html.Div("Waiting for first update...", className="empty-state"))
    return cards


def _build_positions_table(snapshots: Dict[str, AccountSnapshot]):
    rows: List[dict] = []
    for name, snapshot in snapshots.items():
        for position in snapshot.open_positions:
            rows.append(
                {
                    "broker": name,
                    "symbol": position.symbol,
                    "quantity": position.quantity,
                    "pnl": position.pnl,
                }
            )
    return rows


def _build_pnl_history():
    figure = go.Figure()
    has_traces = False
    for broker in store.brokers():
        history = list(store.get_history(broker))
        if not history:
            continue
        has_traces = True
        df = pd.DataFrame(
            {
                "timestamp": [snap.timestamp for snap in history],
                "pnl": [snap.pnl for snap in history],
            }
        )
        figure.add_trace(
            go.Scatter(x=df["timestamp"], y=df["pnl"], mode="lines+markers", name=broker)
        )
    if not has_traces:
        figure.add_annotation(
            text="No data yet", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False
        )
    figure.update_layout(
        title="PnL Trend", xaxis_title="Timestamp (UTC)", yaxis_title="PnL", template="plotly_white"
    )
    return figure


def _format_last_updated(snapshots: Dict[str, AccountSnapshot]) -> str:
    if not snapshots:
        return "Last update: pending"
    latest_ts = max(snapshot.timestamp for snapshot in snapshots.values())
    return f"Last update: {latest_ts.strftime('%Y-%m-%d %H:%M:%S')} UTC"


app = make_dash_app()
server = app.server


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
