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
from plotly import tools

Y1 = deque(maxlen=1800)
Y2 = deque(maxlen=1800)
Y1.append(scrape()[0])
Y2.append(scrape()[1])
X = deque(maxlen=1800)
X.append(datetime.datetime.now())

app = dash.Dash(__name__)
app.layout = html.Div([
		html.Div(
			className='app-header',
			children=[
				html.Div('GoDaddy Live Queue', className='app-header--title')
			]
		),
		html.Div(
			className='app-metrics',
			children=[
				html.Div(id='live-update-text', className='app-metrics--live')
			]
		),
        dcc.Graph(id='live-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*4000
        ),
    ]
)

@app.callback(Output('live-update-text', 'children'),
              events=[Event('interval-component', 'interval')])
def update_metrics():
	Y1.append(scrape()[0])
	Y2.append(scrape()[1])
	X.append(datetime.datetime.now())
	
	return [
		html.Span('Test: {}'.format(Y1[-1]))
	]

@app.callback(Output('live-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_scatter():
	Y1.append(scrape()[0])
	Y2.append(scrape()[1])
	X.append(datetime.datetime.now())
	
	if (int(list(Y1)[0]) == 0):
		diff = "-.--%"
	else:
		diff = str(round(((int(list(Y1)[-1]) - int(list(Y1)[0])) / int(list(Y1)[0])) * 100, 2)) + "%"
	
	if (int(list(Y2)[0]) == 0):
		diff2 = "-.--%"
	else:
		diff2 = str(round(((int(list(Y2)[-1]) - int(list(Y2)[0])) / int(list(Y2)[0])) * 100, 2)) + "%"

	# ============================================
	# graph elements for the regular inbound queue
	# ============================================
	data1 = plotly.graph_objs.Scatter(
		x=list(X),
		y=list(Y1),
		name='Inbound Queue',
		mode= 'lines',
		fill='tozeroy',
		line = dict(color='rgb(0, 255, 242)')
	)
	line1 = plotly.graph_objs.Scatter(
		x=[list(X)[0], list(X)[-1]],
		y=[list(Y1)[0], list(Y1)[-1]],
		name = "Inbound 1H Diff",
		line = dict(
			color = '#ff0101',
			width = 2,
			dash = 'dot'
		),
		yaxis='y3'
	)
	# ============================================
	# graph elements for the regular french queue
	# ============================================
	data2 = plotly.graph_objs.Scatter(
		x=list(X),
		y=list(Y2),
		name='French Queue',
		mode= 'lines',
		fill='tozeroy',
		yaxis='y2',
		line = dict(color='rgb(255, 94, 225)')
	)
	line2 = plotly.graph_objs.Scatter(
		x=[list(X)[0], list(X)[-1]],
		y=[list(Y2)[0], list(Y2)[-1]],
		name = "French 1H Diff",
		line = dict(
			color = '#ffff00',
			width = 2,
			dash = 'dot'
		),
		yaxis='y4'
	)

	annotations=[
        dict(
			xref='x',
			yref='y',
			x=list(X)[-1],
            y=list(Y1)[-1],
            text=str(list(Y1)[-1]),
            showarrow=False,
			font=dict(
				size=40,
				family='Monaco, monospace',
				color='rgb(0, 255, 242)'
			),
			ax=-1000,
			ay=-10
		),
		dict(
			xref='x',
			yref='y2',
			x=list(X)[-1],
			y=list(Y2)[-1],
			text=str(list(Y2)[-1]),
			showarrow=False,
			font=dict(
				size=40,
				family='Monaco, monospace',
				color='rgb(255, 94, 225)'
			),
			ax=-1000,
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
	
	# add the the new plots to the figure
	fig.append_trace(data1, 1, 1)
	fig.append_trace(line1, 1, 1)
	fig.append_trace(data2, 2, 1)
	fig.append_trace(line2, 2, 1)
	fig.append_trace(line3, 1, 1)
	
	# design of the live graph
	fig['layout'].update(
		annotations=annotations,
		paper_bgcolor='rgb(61, 61, 61)',
		plot_bgcolor='rgb(61, 61, 61)',
		margin=go.Margin(
			t=20
		),
		height=850,
		showlegend=False,
		xaxis=dict(
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			range=[min(X), max(X)],
			linecolor='black',
			linewidth=2,
			tickwidth=2,
			showticklabels=False,
		),
		xaxis2=dict(
			color='lightgrey',
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			ticks='outside',
			title=str(datetime.datetime.now().time()),
			range=[min(X), max(X)],
			linecolor='black',
			linewidth=2,
			tickwidth=2,
		),
		yaxis=dict(
			color='rgb(0, 226, 215)',
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			ticks='outside',
			title='INBOUND (' + diff + ')',
			titlefont=dict(
				family='Lucida Sans Unicode", "Lucida Grande", sans-serif',
				color='rgb(0, 226, 215)',
				size=20
			),
			range=[0, 350],
			linecolor='black',
			linewidth=2,
			mirror='ticks',
			tickwidth=2,
			side='left'
		),
		yaxis2=dict(
			color='rgb(255, 94, 225)',
			tickcolor='black',
			gridcolor='rgb(112, 112, 112)',
			ticks='outside',
			title='FRENCH (' + diff2 + ')',
			titlefont=dict(
				family='Lucida Sans Unicode", "Lucida Grande", sans-serif',
				color='rgb(255, 94, 225)',
				size=20
			),
			range=[0, 15],
			linecolor='black',
			linewidth=2,
			mirror='ticks',
			tickwidth=2,
			side='left'
		)
	)
	
	return(fig)

if __name__ == '__main__':
    app.run_server(debug=True)
