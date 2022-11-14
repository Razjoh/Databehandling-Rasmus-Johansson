from dash import html, dcc
import dash_bootstrap_components as dbc

class Layout:
    def __init__(self, symbol_dict: dict) -> None:
        self._symbol_dict = symbol_dict

        self._stock_options_dropdown = [
            {"label": name, "value": symbol} for symbol, name in symbol_dict.items()
        ]
        self._ohlc_options = [
            {"label": option, "value": option} for option in ("open", "high", "low", "close")
        ]
        self._slider_marks = {
            i: mark
            for i, mark in enumerate(
                ["1 Day", "1 Week", "1 Month", "3 Months", "1 Year", "5 Years", "Max"]
            )
        }
    
    def layout(self):
        return dbc.Container(
            [
                dbc.Card(dbc.CardBody(html.H1("Techy stocks viewer")), className="mt-3"),

                dbc.Row([
                    dbc.Col(html.P("Choose a stock")),

                    dbc.Col(dcc.Dropdown(
                    id="stockpicker-dropdown",
                    options=self._stock_options_dropdown,
                    value="AAPL",
                )),
                
                    dbc.Col()
                ]),

                
                html.P(id = "highest-value"),
                html.P(id = "lowest-value"),
                dcc.RadioItems(id="ohlc-radio", options=self._ohlc_options, value="close"),
                dcc.Graph(id="stock-graph"),
                dcc.Slider(
                    id="time-slider", min=0, max=6, marks=self._slider_marks, value=2, step=None
                ),
                # storing intermediate value on clients browser in order to share between several callbacks
                dcc.Store(id = "filtered-df")
            ]
)

