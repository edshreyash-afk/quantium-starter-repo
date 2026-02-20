import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
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
                    style={
                        "textAlign": "center",
                        "marginBottom": "10px",
                        "color": "#2d3748"
                    }
                ),

                html.P(
                    "Explore sales trends before and after the January 15th, 2021 price change.",
                    style={
                        "textAlign": "center",
                        "color": "#4a5568",
                        "marginBottom": "25px"
                    }
                ),

                html.Div(
                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "marginBottom": "20px"
                    },
                    children=[
                        dcc.RadioItems(
                            id="region-selector",
                            options=[
                                {"label": " All", "value": "all"},
                                {"label": " North", "value": "north"},
                                {"label": " East", "value": "east"},
                                {"label": " South", "value": "south"},
                                {"label": " West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={
                                "fontSize": "16px",
                                "color": "#2d3748"
                            }
                        )
                    ]
                ),

                dcc.Graph(id="sales-chart")

            ]
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    daily_sales = (
        filtered
        .groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        markers=True,
        labels={
            "date": "Date",
            "sales": "Total Sales ($)"
        },
        title="Daily Pink Morsel Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)