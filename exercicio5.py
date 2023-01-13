import plotly.express as px
import pandas as pd


# reading the database
data = pd.read_csv("company_sales_data.csv")

fig = px.scatter(data, x="month_number", y="toothpaste", labels={"toothpaste": "Sales units in number"})

fig.update_traces(marker_size=15)

fig.update_xaxes(showgrid=True, gridwidth=1, griddash="dash", gridcolor="grey")
fig.update_yaxes(showgrid=True, gridwidth=1, griddash="dash", gridcolor="grey")

fig.show()