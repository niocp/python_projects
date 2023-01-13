import plotly.express as px
import pandas as pd


# reading the database
data = pd.read_csv("company_sales_data.csv")

fig = px.histogram(data, x="total_profit", title="Profit data",
             labels={"bathingsoap": "Sales units in number", "month_number": "Month Number"})

fig.update_xaxes(showgrid=True, gridwidth=1, griddash="dash", gridcolor="grey")
fig.update_yaxes(showgrid=True, gridwidth=1, griddash="dash", gridcolor="grey")

fig.show()