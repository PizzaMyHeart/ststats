#!/usr/bin/python3

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

app = dash.Dash(__name__,     
				meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])

app.title = 'ST Stats'

cwd = os.path.dirname(__file__)

filepath = os.path.join(cwd, 'data/data.csv')

df = pd.read_csv(filepath).drop('Unnamed: 0', axis=1)

colours = {'background': '#05192d'}




app.layout = html.Div(children=[
	html.Div(id='top', children=[
		html.H1(children='Specialty Training Stats'),
		
		dcc.Dropdown(
	    	id='level-dropdown',

	    	options=[
	    		{'label': 'CT1/ST1', 'value': 1},
	    		{'label': 'ST3', 'value': 3},
	    		{'label': 'ST4', 'value': 4}
	    	],

	    	value=1,

	    	style={
	    		'color': 'black',
	    		'width': '7em',
	    		'marginLeft': '2em'
	    	},

	    	clearable=False),

		html.Div(html.A(href='#', children=['About']), style={'marginLeft': 'auto', 'marginRight': '3em'}),

		html.Div(html.A(href='#how', children=['Help']), style={'marginRight': 0}) 

		]
	),

    html.Div(
    	children=[
	    dcc.Graph(
	        id='ratio-year-fig',
	        config={'modeBarButtonsToRemove': ['select2d', 'lasso2d', 'hoverClosestCartesian', 'hoverCompareCartesian', 'toggleSpikelines'],
	        		'displaylogo': False}
	        # The 'figure' property is updated via the callback below
	    )]
    ),

    html.Div(
    	children=[
    	dcc.Graph(
    		id='one-year-fig',
	        config={'modeBarButtonsToRemove': ['select2d', 'lasso2d', 'hoverClosestCartesian', 'hoverCompareCartesian', 'toggleSpikelines'],
	        		'displaylogo': False}
    		)], 

    	style={'display': 'inline-block'}
    ),

    html.Div(
    	children=[
    	dcc.Graph(
    		id='all-years-specialty',
	        config={'modeBarButtonsToRemove': ['select2d', 'lasso2d', 'hoverClosestCartesian', 'hoverCompareCartesian', 'toggleSpikelines'],
	        		'displaylogo': False}
    	)],

    	style={'display': 'inline-block',
    			'marginRight': 0}),

    html.Div(children=[
    	html.H3(id='how', children=['How to use:']),
    	html.P('1. Select the recruitment level (CT/ST1, ST3, ST4) from the dropdown box.'),
    	html.P('2. Double-click or double-tap quickly on the desired specialty in the legend on the right-hand side of the first chart. '),
    	html.P('3. Click or tap once on other specialties you want to add to the chart.'),
    	html.P('4. Click on data points on the first chart to view specific information for that specialty in the bottom two charts.'),
    	html.P('5. Hover over bars and lines to view more information.'),
    	html.P('Data source: Health Education England'),
    	html.P('Send your comments and suggestions to zchaijt at ucl dot ac dot uk', style={'fontStyle': 'italic'}),
    	html.A(href='#top', children=['Back to top ^']), 
    	]),

    html.Footer(children=[html.P(children=['More fun stuff: ' , 
    								html.A(href='https://muler.pythonanywhere.com', children='Muler'),
    								'    |   ',
    								html.A(href='https://tachy.org/', children='Tachy')])
    						])


])

############################
#	Callbacks			   #
############################

@app.callback(
	Output(component_id='ratio-year-fig', component_property='figure'),
	Input(component_id='level-dropdown', component_property='value')
)
def update_ratio_year_fig(level):
	'''Returns a Graph object
	Accepts dropdown value (level) as input and returns a line chart of the dataframe filtered on level.
	'''


	# Need to sort dataframe by year, otherwise points are joined out of sequence.
	filtered_df = df[df['level']==level].sort_values(by='year')

	
	ratio_year = px.line(filtered_df, 
						x='year', y='ratio', 
						hover_name='specialty',
						title='Competition Ratios 2013 - 2020', 
						labels={'year': 'Year', 'ratio': 'Ratio', 'specialty': 'Specialty'},
						color='specialty', 
						template='plotly_dark')

	ratio_year.update_layout(
		plot_bgcolor=colours['background'],
		paper_bgcolor=colours['background'],
		xaxis_fixedrange=True,
		yaxis_fixedrange=True)

	ratio_year.update_traces(mode='lines+markers')

	return ratio_year

@app.callback(
	Output(component_id='one-year-fig', component_property='figure'),
	Output(component_id='all-years-specialty', component_property='figure'),
	Input(component_id='level-dropdown', component_property='value'),
	Input(component_id='ratio-year-fig', component_property='clickData')
)
def update_one_year_fig(level, clickData):
	'''
	'''
	specialty = ''
	clrs = []
	# Default year is 2020 on initialisation
	if clickData:
		#print(clickData)
		year = clickData['points'][0]['x']
		specialty = clickData['points'][0]['hovertext'] 

	else:
		year = 2020
	
	filtered_df_year = df[(df['level']==level) & (df['year']==year)].sort_values(by='ratio')

	one_year = px.bar(filtered_df_year, 
						x='ratio', y='specialty',
						hover_name='specialty',
						labels={'year': 'Year', 'ratio': 'Ratio', 'specialty': 'Specialty'},
						title=f'Competition Ratios in {year}',
						template='plotly_dark')

	# Store these before removing yaxis labels
	y_array = one_year.data[0].y
	clrs = ['blue']*len(y_array)

	one_year.update_layout(
		plot_bgcolor=colours['background'],
		paper_bgcolor=colours['background'],
		yaxis_showticklabels=False,
		xaxis_fixedrange=True,
		yaxis_fixedrange=True)
	

	for y in y_array:
		if y == specialty:
			print('Matched', specialty)
			clrs[list(y_array).index(y)] = 'orange'
	
	one_year.update_traces(marker=dict(color=clrs))


	# Applications and posts for given specialty
	filtered_df_specialty = df[(df['level']==level) & (df['specialty']==specialty)].sort_values(by='year')

	all_years = make_subplots()

	all_years.add_trace(go.Scatter(
						x=filtered_df_specialty['year'], y=filtered_df_specialty['applications'],
						name='Applications'),
	)


	all_years.add_trace(go.Scatter(
						x=filtered_df_specialty['year'], y=filtered_df_specialty['posts'],
						name='Posts')
	)

	all_years.update_layout(
		title=f'{specialty} Applications and Posts',
		template='plotly_dark',
		plot_bgcolor=colours['background'],
		paper_bgcolor=colours['background'],
		xaxis_fixedrange=True,
		yaxis_fixedrange=True,
		xaxis_title='Year',
		legend={'orientation': 'h'})

	return one_year, all_years
'''
@app.callback(
	Output(component_id='all-years-specialty', component_property='figure'),
	Input(component_id='level-dropdown', component_property='value'),
	Input(component_id='ratio-year-fig', component_property='clickData')
	)
'''
if __name__ == '__main__':
	app.run_server(debug=True, host='0.0.0.0')