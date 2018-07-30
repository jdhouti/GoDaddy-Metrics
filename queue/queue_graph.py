import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import pandas as pd

# Create the dataframe
number_of_csvs = 1
df_list, data = [], []
for i in range(number_of_csvs):
	df_list.append(pd.read_csv('queuetimes' + str(i) + '.csv'))
	df_list[i]['time'] = pd.to_datetime(df_list[i]['time'])

# Create traces
for i in df_list:
	data.append(
		go.Scatter(
			x=i['time'],
			y=i['callers'],
			mode='lines',
			marker=dict(
				color='rgb(65, 190, 244)'
			)
		)
	)
	data.append(
		go.Scatter(
			x=i['time'],
			y=i['agents'],
			mode='lines',
			marker=dict(
				color='rgb(244, 164, 66)'
			)
		)
	)

# Edit the layout
layout = go.Layout(
	title='Queue Customer Count Throughout the Day',
	xaxis=dict(
		title='TIME'
	),
	yaxis=dict(
		title='NUMBER OF PEOPLE'
	),
	showlegend=False
)

# Create the figure
figure = go.Figure(data=data, layout=layout)

# plot the graph
plotly.offline.plot(figure)

input()