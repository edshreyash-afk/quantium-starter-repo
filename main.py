import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load formatted sales data
df = pd.read_csv("formatted_sales.csv")

# Convert date to datetime and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Aggregate sales per day
daily_sales = df.groupby("date", as_index=False)["sales"].sum()

# Create line chart
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

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == "__main__":
    app.run(debug=True)
