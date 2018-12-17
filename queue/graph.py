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

# df_colors = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, df.columns.size)]
df_colors = ['rgb(0, 255, 242)', 'rgb(57, 255, 20)', 'rgb(255, 94, 225)']
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
	title='General Queue Report for ' + str(datetime.datetime.now().date()),
        paper_bgcolor='rgb(61, 61, 61)',
        plot_bgcolor='rgb(61, 61, 61)',
        titlefont=dict(
            family='Lucida Sans Unicode", "Lucida Grande", sans-serif',
            color='lightgrey'
        ),
        legend=dict(
                font=dict(
                        family='Lucida Sans Unicode", "Lucida Grande", sans-serif',
                        color='lightgrey'
                ),
        ),
	xaxis=dict(
		title='TIME',
		zeroline=True,
                linecolor='black',
                gridcolor='rgb(112, 112, 112)',
                linewidth=2,
                tickwidth=2,
                ticks='outside',
                tickcolor='black',
                color='lightgrey'
	),
	yaxis=dict(
		showline=True,
		zeroline=True,
		title='PEOPLE',
                linecolor='black',
                gridcolor='rgb(112, 112, 112)',
                linewidth=2,
                tickwidth=2,
                ticks='outside',
                tickcolor='black',
                color='lightgrey'
	)
)

figure = go.Figure(layout=layout, data=data)

image_name = str(datetime.datetime.now().date()) + '_report'
plotly.offline.plot(figure, filename=(image_name + '.html'))
print('info : report generated.')
