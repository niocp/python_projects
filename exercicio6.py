import plotly.express as px
import pandas as pd


# reading the database
data = pd.read_csv("company_sales_data.csv")

fig = px.bar(data, x="month_number", y=data.columns[1:3], barmode='group',
             labels={"value": "Sales units in number", "month_number": "Month Number"})

fig.update_xaxes(showgrid=True, gridwidth=1, griddash="dash", gridcolor="grey")
fig.update_yaxes(showgrid=True, gridwidth=1, griddash="dash", gridcolor="grey")

fig.show()