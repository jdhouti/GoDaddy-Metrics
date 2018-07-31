import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import datetime

# Create the dataframe
def create_graph(frame):
	"""Creates the graph object and returns a go.Figure object."""
	df = pd.read_csv(frame)
	df.columns = ['callers', 'agents', 'french', 'time']
	df['time'] = pd.to_datetime(df['time'])
	data = []

	# Create traces
	data.append(
		go.Scatter(x=df['time'], y=df['callers'], mode='lines',
			marker=dict(
				color='rgb(65, 190, 244)'
			),
			name='Inbound'
		)
	)
	data.append(
		go.Scatter(x=df['time'], y=df['agents'], mode='lines',
			marker=dict(
				color='rgb(244, 164, 66)'
			),
			name='Agents'
		)
	)
	data.append(
		go.Scatter(x=df['time'], y=df['french'], mode='lines',
			marker=dict(
				color='rgb(244, 66, 89)'
			),
			name='French'
		)
	)
	# Edit the layout
	layout = go.Layout(
		title='Queue Report for ' + str(datetime.datetime.now().date()),
		xaxis=dict(
			title='TIME'
		),
		yaxis=dict(
			title='NUMBER OF PEOPLE'
		)
	)
	return go.Figure(data=data, layout=layout)