import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# reading the database
data = pd.read_csv("company_sales_data.csv")

fig = make_subplots(rows=2, cols=1, subplot_titles=("Sales data of a Bathingsoup", "Sales data of a facewash"))

fig.add_trace(
    go.Line(x=data["month_number"], y=data["bathingsoap"]),
    row=1, col=1
)

fig.add_trace(
    go.Line(x=data["month_number"], y=data["facewash"]),
    row=2, col=1
)


fig.show()