import plotly.express as px
import pandas as pd

# reading the database
data = pd.read_csv("company_sales_data.csv")

salesData = [data['facecream'].sum(), data['facewash'].sum(), data['toothpaste'].sum(),
         data['bathingsoap'].sum(), data['shampoo'].sum(), data['moisturizer'].sum()]

fig = px.pie(data, values=salesData, names=data.columns[1:7], title="Sales data")

fig.update_traces(textinfo='percent', textfont_size=20,
                  marker=dict(line=dict(color='#000000', width=2)))

fig.show()