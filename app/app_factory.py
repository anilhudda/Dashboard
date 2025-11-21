from __future__ import annotations

from typing import Dict, List, Sequence, Tuple

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, Input, Output, dash_table, dcc, html

from app.clients.base import BrokerClient
from app.models.account_snapshot import AccountSnapshot
from app.services.aggregator import Aggregator
from app.services.data_store import DataStore


def create_dashboard_app(
    clients: Sequence[BrokerClient],
    refresh_seconds: int,
    history_limit: int = 1440,
    start_scheduler: bool = False,
) -> Tuple[Dash, Aggregator, DataStore]:
    """Factory that wires the Dash app, store, and aggregator together."""

    store = DataStore(history_limit=history_limit)
    aggregator = Aggregator(clients=clients, store=store, refresh_seconds=refresh_seconds)

    if start_scheduler:
        aggregator.start()

    app = Dash(__name__)
    app.title = "Broker PnL Monitor"

    app.layout = html.Div(
        [
            html.H1("Multi-Broker Trading Dashboard", className="app-title"),
            html.Div(id="last-updated", className="last-updated"),
            dcc.Interval(id="data-refresh", interval=refresh_seconds * 1000, n_intervals=0),
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

    def _build_cards(snapshots: Dict[str, AccountSnapshot]):
        cards: List[html.Div] = []
        for name, snapshot in sorted(snapshots.items()):
            cards.append(
                html.Div(
                    [
                        html.H3(name, className="card-title"),
                        html.Div(
                            [
                                html.Span("PnL"),
                                html.Strong(f"₹ {snapshot.pnl:,.2f}"),
                            ],
                            className="card-row",
                        ),
                        html.Div(
                            [
                                html.Span("Net Margin"),
                                html.Strong(f"₹ {snapshot.net_margin:,.2f}"),
                            ],
                            className="card-row",
                        ),
                        html.Div(
                            [
                                html.Span("Available Margin"),
                                html.Strong(f"₹ {snapshot.available_margin:,.2f}"),
                            ],
                            className="card-row",
                        ),
                        html.Div(
                            [
                                html.Span("Orders"),
                                html.Strong(str(snapshot.order_count)),
                            ],
                            className="card-row",
                        ),
                        html.Div(
                            [
                                html.Span("Open Positions"),
                                html.Strong(str(len(snapshot.open_positions))),
                            ],
                            className="card-row",
                        ),
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

    return app, aggregator, store


__all__ = ["create_dashboard_app"]
