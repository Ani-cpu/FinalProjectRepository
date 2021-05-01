import io
from base64 import b64encode

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import plotly.graph_objs as go





buffer = io.StringIO()

df1 = pd.read_csv('../Datasets/ElectricCarData_Clean.csv')
fig = px.bar(df1, x="Model", y="PriceEuro", color="Brand", title="Price of Models in specified Brand").update_xaxes(categoryorder="total descending")
fig2 = px.bar(df1, x="Model", y="AccelSec", color="Brand", title="Which car can accelerate the fastest?").update_xaxes(categoryorder="total descending")

fig3 = px.bar(df1, x="Model", y="Range_Km", color="Brand", title="Which car gives you the best range?").update_yaxes(categoryorder="total descending")
fig4 = px.bar(df1, x="Model", y="Efficiency_WhKm", color="Brand", title="Which car gives you the best efficiency. How much energy needed to move 1 unit?").update_yaxes(categoryorder="total descending")
fig5 = px.bar(df1, x="Model", y="FastCharge_KmH", color="Brand", title="How fast can you car charged?. ").update_yaxes(categoryorder="total descending")
fig6 = px.bar(df1, x="Model", y="Seats", color="Model", title="How many seats are in your car?. ").update_yaxes(categoryorder="total descending")




fig.update_layout(
    margin=dict(l=20, r=20, t=100, b=0),
    paper_bgcolor="LightSteelBlue",
)
fig2.update_layout(
    margin=dict(l=20, r=20, t=100, b=0),
    paper_bgcolor="LightSteelBlue",
)
fig3.update_layout(
    margin=dict(l=20, r=20, t=100, b=0),
    paper_bgcolor="LightSteelBlue",
)
fig4.update_layout(
    margin=dict(l=20, r=20, t=100, b=0),
    paper_bgcolor="LightSteelBlue",
)
fig5.update_layout(
    margin=dict(l=20, r=20, t=100, b=0),
    paper_bgcolor="LightSteelBlue",
)
fig6.update_layout(
    margin=dict(l=20, r=20, t=100, b=0),
    paper_bgcolor="LightSteelBlue",
)

fig.write_html(buffer)
fig2.write_html(buffer)
fig3.write_html(buffer)
fig4.write_html(buffer)
fig5.write_html(buffer)
fig6.write_html(buffer)


html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1(children='EcoChoice: The web app to help you find your next electric vehicle'),
    html.H3(children='By: Anirudh. Adam, Dylan, Lamar'),
    dcc.Graph(id="graph", figure=fig),
    dcc.Graph(id="graph2",figure=fig2),
    dcc.Graph(id="graph3",figure=fig3),
    dcc.Graph(id="graph4",figure=fig4),
    dcc.Graph(id="graph5",figure=fig5),
    dcc.Graph(id="graph6",figure=fig6)
])

app.run_server(debug=True)