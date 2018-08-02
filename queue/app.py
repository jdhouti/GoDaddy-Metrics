import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from scrapeFunc import scrape
import datetime

Y = deque(maxlen=28800)
Y.append(scrape())
X = deque(maxlen=28800)
X.append(datetime.datetime.now())


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph'),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    Y.append(scrape())
    X.append(datetime.datetime.now())

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Inbound Queue',
            mode= 'lines'
    )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X), max(X)]),
												yaxis=dict(range=[0, 300]))}

if __name__ == '__main__':
    app.run_server(debug=True)