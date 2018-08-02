import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly
import datetime
import numpy as np
import sys

data_filename = 'queue_data_' + str(datetime.datetime.now().date()) + '.csv'
print('info : generating report for ' + data_filename)

try:
	df = pd.read_csv(data_filename)
	df.columns = ['Inbound', 'Agents', 'French', 'time']
	df['time'] = pd.to_datetime(df['time'])
except:
	print('error: could not generate report :(')
	input()
	sys.exit()

df_colors = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, df.columns.size)]
data, annotations = [], []

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

for i in df.columns[:-1]:
	max_index = df[i].idxmax
	annotations.append(
		dict(
			x=df['time'][max_index],
			y=df[i][max_index],
			xref='x',
			yref='y',
			text='peak: ' + str(df[i][max_index]),
			showarrow=True,
			arrowhead=1,
			ax=0,
			ay=-40
		)
	)

# Edit the layout
layout = go.Layout(
	annotations=annotations,
	title='Queue Report for ' + str(datetime.datetime.now().date()),
	xaxis=dict(
		title='TIME',
		zeroline=True,
	),
	yaxis=dict(
		showline=True,
		zeroline=True,
		title='NUMBER OF PEOPLE',
	)
)

figure = go.Figure(layout=layout, data=data)

image_name = str(datetime.datetime.now().date()) + '_report'
plotly.offline.plot(figure, filename=(image_name + '.html'))
print('info : report generated.')