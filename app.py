from src.seir import SEIR
import plotly.graph_objs as go
from scipy.integrate import odeint
from dash import dcc
from dash.dependencies import Input, Output
import numpy as np
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash

load_figure_template("CYBORG")
S0 = 999
E0 = 0
I0 = 1
R0 = 0
N = S0 + E0 + I0 + R0
days = 100


def create_fig(N, S0, E0, I0, R0, beta, sigma, gamma, days):
    y0 = S0, E0, I0, R0
    t = np.linspace(0, int(days), int(days))
    ret = odeint(SEIR, y0, t, args=(N, beta, sigma, gamma))
    S, E, I, R = ret.T

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=S, mode="lines", name="Susceptible"))
    fig.add_trace(go.Scatter(x=t, y=E, mode="lines", name="Exposed"))
    fig.add_trace(go.Scatter(x=t, y=I, mode="lines", name="Infectious"))
    fig.add_trace(go.Scatter(x=t, y=R, mode="lines", name="Recovered"))
    fig.update_layout(
        title="SEIR Model Simulation", xaxis_title="Days", yaxis_title="Population"
    )
    return fig


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="seir-graph", style={"height": "90vh", "width": "100%"}),
                html.Div(
                    id="output",
                    style={
                        "marginTop": "20px",
                        "fontSize": "18px",
                        "fontWeight": "bold",
                        "textAlign": "center",
                    },
                ),
            ],
            style={"float": "left", "width": "70%", "height": "120vh"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("S", style={"marginRight": "10px"}),
                        dcc.Input(
                            id="s-input",
                            type="number",
                            value=S0,
                            style={"marginRight": "20px"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("E", style={"marginRight": "10px"}),
                        dcc.Input(
                            id="e-input",
                            type="number",
                            value=E0,
                            min=0,
                            max=N,
                            style={"marginRight": "20px"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("I", style={"marginRight": "10px"}),
                        dcc.Input(
                            id="i-input",
                            type="number",
                            value=I0,
                            min=0,
                            max=N,
                            style={"marginRight": "20px"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("R", style={"marginRight": "10px"}),
                        dcc.Input(
                            id="r-input",
                            type="number",
                            value=R0,
                            min=0,
                            max=N,
                            style={"marginRight": "20px"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("Days", style={"marginRight": "10px"}),
                        dcc.Input(
                            id="days-input",
                            type="number",
                            value=days,
                            min=0,
                            style={"marginRight": "20px"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("Beta", style={"marginRight": "10px"}),
                        dcc.Slider(
                            id="beta-slider",
                            min=0,
                            max=1,
                            step=0.01,
                            value=0.3,
                            marks={0: "0", 0.5: "0.5", 1: "1"},
                            tooltip={"always_visible": True, "placement": "bottom"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("Sigma", style={"marginRight": "10px"}),
                        dcc.Slider(
                            id="sigma-slider",
                            min=0,
                            max=1,
                            step=0.01,
                            value=0.2,
                            marks={0: "0", 0.5: "0.5", 1: "1"},
                            tooltip={"always_visible": True, "placement": "bottom"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("Gamma", style={"marginRight": "10px"}),
                        dcc.Slider(
                            id="gamma-slider",
                            min=0,
                            max=1,
                            step=0.01,
                            value=0.1,
                            marks={0: "0", 0.5: "0.5", 1: "1"},
                            tooltip={"always_visible": True, "placement": "bottom"},
                        ),
                    ],
                    style={"marginBottom": "20px"},
                ),
            ],
            style={
                "float": "right",
                "width": "30%",
                "padding": "20px",
                "height": "100vh",
            },
        ),
    ],
    style={"maxWidth": "1200px", "margin": "auto"},
)


@app.callback(
    Output("seir-graph", "figure"),
    [
        Input("s-input", "value"),
        Input("e-input", "value"),
        Input("i-input", "value"),
        Input("r-input", "value"),
        Input("days-input", "value"),
        Input("beta-slider", "value"),
        Input("sigma-slider", "value"),
        Input("gamma-slider", "value"),
    ],
)
def update_figure(S0, E0, I0, R0, days, beta, sigma, gamma):
    N = S0 + E0 + I0 + R0
    fig = create_fig(N, S0, E0, I0, R0, beta, sigma, gamma, days)
    return fig


if __name__ == "__main__":
    app.run_server(debug=False)
