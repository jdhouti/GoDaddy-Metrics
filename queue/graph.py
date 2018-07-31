import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly
import datetime
import numpy as np

data_filename = 'queue_data_' + str(datetime.datetime.now().date()) + '_test.csv'

# Create the dataframe
def create_graph(frame):
	"""Returns a go.Figure object."""
	df = pd.read_csv(frame)
	df.columns = ['Inbound', 'Agents', 'French', 'time']
	df_colors = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, df.columns.size)]
	df['time'] = pd.to_datetime(df['time'])
	data = []

	# Create traces
	for i in df.columns[:-1]:
		data.append(
			go.Scatter(
				x=df['time'],
				y=df[i],
				mode='lines',
				marker=dict(
					color=df_colors[list(df.columns).index(i)]
				),
				name=i
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

try:
    print('info : generating report for ' + data_filename)
    #create the graph
    final_graph = create_graph(data_filename)

    # plot the graph and save the graph
    image_name = str(datetime.datetime.now().date()) + '_report'
    plotly.offline.plot(final_graph, filename=(image_name + '.html'))
    print('info : report generated.')
except:
    print('error: could not generate report :(')
    input()