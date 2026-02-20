import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    # Radio buttons
    dcc.RadioItems(
        id="region-selector",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",  # default selection
        inline=True
    ),

    dcc.Graph(id="sales-chart")
])


# Callback to update chart
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Aggregate daily sales
    daily_sales = (
        filtered_df
        .groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        labels={
            "date": "Date",
            "sales": "Total Sales ($)"
        },
        title="Pink Morsel Sales Over Time"
    )

    return fig


# Run server
if __name__ == "__main__":
    app.run(debug=True)