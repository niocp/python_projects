import plotly.express as px
import pandas as pd


# reading the database
data = pd.read_csv("company_sales_data.csv")

fig = px.line(data, x="month_number", y="total_profit", title='Company profit per month',
              labels={"month_number": "Month Number", "total_profit": "Sold units number"}, markers=True)

fig.update_traces(line=dict(color='red', width=3, dash='dash'),
                  marker=dict(size=12, color='black', line=dict(width=2, color='red')))

fig.update_layout(
   legend_title="legend",
   font=dict(
      family="Arial",
      size=20,
   ))

# showing the plot
fig.show()
