import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("company_sales_data.csv")

fig = px.line()

fig.add_trace(go.Scatter(
    name="Face cream",
    x=data["month_number"],
    y=data["facecream"],
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name="Face wash",
    x=data["month_number"],
    y=data["facewash"],
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name="Tooth paste",
    x=data["month_number"],
    y=data["toothpaste"],
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name="Bathing soap",
    x=data["month_number"],
    y=data["bathingsoap"],
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name="Shampoo",
    x=data["month_number"],
    y=data["shampoo"],
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name="Moisturizer",
    x=data["month_number"],
    y=data["moisturizer"],
    stackgroup='one'
))
fig.show()