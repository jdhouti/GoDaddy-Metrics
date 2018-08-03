import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from scrapeFunc_test import scrape
import datetime
from plotly import tools

Y1 = deque(maxlen=3600)
Y2 = deque(maxlen=3600)
Y1.append(scrape()[0])
Y2.append(scrape()[1])
X = deque(maxlen=3600)
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
	Y1.append(scrape()[0])
	Y2.append(scrape()[1])
	X.append(datetime.datetime.now())

	data1 = plotly.graph_objs.Scatter(
			x=list(X),
			y=list(Y1),
			name='Inbound Queue',
			mode= 'lines',
			line = dict(color='rgb(0, 255, 242)')
	)
	data2 = plotly.graph_objs.Scatter(
			x=list(X),
			y=list(Y2),
			name='French Queue',
			mode= 'lines',
			yaxis='y2',
			line = dict(color='rgb(255, 94, 225)')
	)
	
	annotations=[
        dict(
            x=list(X)[-1],
            y=list(Y1)[-1],
            xref='x',
            yref='y',
            text=str(list(Y1)[-1]),
            showarrow=False,
			font=dict(
				size=20,
				family='Monaco, monospace',
                color='rgb(0, 255, 242)'
            ),
            ax=30,
            ay=-10
        ),
        dict(
            x=list(X)[-1],
            y=list(Y2)[-1],
            xref='x',
            yref='y2',
            text=str(list(Y2)[-1]),
            showarrow=False,
			font=dict(
				size=20,
				family='Monaco, monospace',
                color='rgb(255, 94, 225)'
            ),
            ax=30,
            ay=-10
        )
    ]
	
	fig = tools.make_subplots(
		rows=2,
		cols=1,
		vertical_spacing=0.07,
		subplot_titles=(
			'INBOUND QUEUE: ' + str(scrape()[0]),
			'FRENCH QUEUE: ' + str(scrape()[1])
		)
	)
	
	fig.append_trace(data1, 1, 1)
	fig.append_trace(data2, 2, 1)
	
	fig['layout'].update(
		annotations=annotations,
		paper_bgcolor='rgb(61, 61, 61)',
		plot_bgcolor='rgb(61, 61, 61)',
		margin=go.Margin(
			t=50
		),
		height=900,
		showlegend=False,
		xaxis=dict(
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			range=[min(X), max(X)],
			linecolor='black',
			linewidth=2,
			tickwidth=2,
			showticklabels=False
		),
		xaxis2=dict(
			color='lightgrey',
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			ticks='outside',
			title='TIME: ' + str(datetime.datetime.now().time()),
			range=[min(X), max(X)],
			linecolor='black',
			linewidth=2,
			tickwidth=2
		),
		yaxis=dict(
			color='rgb(0, 226, 215)',
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			ticks='outside',
			title='ENGLISH    CUSTOMERS',
			range=[0, 350],
			linecolor='black',
			linewidth=2,
			mirror='ticks',
			tickwidth=2
		),
		yaxis2=dict(
			color='rgb(255, 94, 225)',
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			ticks='outside',
			title='FRENCH    CUSTOMERS',
			range=[0, 10],
			linecolor='black',
			linewidth=2,
			mirror='ticks',
			tickwidth=2
		)
	)
	
	return(fig)

if __name__ == '__main__':
    app.run_server(debug=True)