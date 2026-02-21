import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data - ensure this file exists in your directory
df = pd.read_csv("formatted_sales.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "background": "linear-gradient(135deg, #667eea, #764ba2)",
        "minHeight": "100vh",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "fontFamily": "Segoe UI"
    },
    children=[
        html.Div(
            id="container",
            style={
                "backgroundColor": "white",
                "borderRadius": "16px",
                "padding": "35px",
                "width": "900px",
                "boxShadow": "0 15px 40px rgba(0,0,0,0.25)"
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales",
                    id="header",
                    style={"textAlign": "center", "color": "#2d3748"}
                ),
                dcc.RadioItems(
                    id="region-picker",
                    options=[
                        {"label": " All", "value": "all"},
                        {"label": " North", "value": "north"},
                        {"label": " East", "value": "east"},
                        {"label": " South", "value": "south"},
                        {"label": " West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                ),
                dcc.Graph(id="sales-graph")
            ]
        )
    ]
)


@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]

    daily_sales = filtered.groupby("date", as_index=False)["sales"].sum().sort_values("date")

    fig = px.line(
        daily_sales, x="date", y="sales", markers=True,
        title="Daily Pink Morsel Revenue"
    )
    fig.update_layout(template="plotly_white", title_x=0.5)
    return fig


if __name__ == "__main__":
    app.run(debug=True)