## `figure` to create a figure for plotting
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
## To displays tooltips whenever the cursor is over a glyph
from bokeh.models.tools import HoverTool
## To apply a client-side CategoricalColorMapper transformation to a ColumnDataSource column
from bokeh.transform import factor_cmap
## To provide a collection of palettes for color mapping
from bokeh.palettes import YlGnBu8
## To return HTML components to embed a Bokeh plot
from bokeh.embed import components
import pandas as pd


## Data
# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]
## Read in CSV data file with Pandas
df = pd.read_csv('cars.csv')

## Create ColumnDataSource from DataFrame
# car = df['Car']
# hp = df['Horsepower']
source = ColumnDataSource(df)

## Name the output HTML file
output_file('index.html')

## Create a list for `y_range` in `figure()`
cars_list = source.data['Car'].tolist()

## Add a plot
p = figure(
	y_range=cars_list,
	plot_width=800,
	plot_height=600,
	title = 'Cars with Top Horsepower',
	# x_axis_label = 'X axis',
	# y_axis_label = 'Y axis',
	## Y-axis is now car names
	x_axis_label = 'Horsepower', 
	## No graph tool displayed
	# tools='' 
	## Add some graph tools
	tools='pan, box_select, zoom_in, zoom_out, save, reset' 
)

## Render glyph
## Add a line graph
# p.line(x, y, legend='Test', line_width=2)
## Add a horizontal bar chart
p.hbar(
	y='Car',
	right='Horsepower',
	left=0,
	## Height of bars
	height=0.4, 
	# color='green',
	## To use different colors for a factor
	fill_color=factor_cmap( 
		'Car',
		palette=YlGnBu8,
		factors=cars_list
	),
	## From 0, light, to 1, dark
	fill_alpha=0.9,
	source=source,
	## Specify factor for legend
	legend_field='Car'
)

## Add legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
## Font size of texts in legend
p.legend.label_text_font_size = '10px'

## Add hover tool to display tooltips
hover = HoverTool()
## When hovering over each bar, car name, price, horsepower and image of the car will be shown
hover.tooltips = """
<div>
	<h3>@Car</h3>
	<div><strong>Price: </strong>@Price</div>
	<div><strong>Horsepower: </strong>@Horsepower</div>
	<div><img src="@Image" alt="Car image" width="200" /></div>
</div>
"""
## Show tools
p.add_tools(hover)

## Show the plot in HTML format
## Each call will open up a new tab in the browser
show(p)
## Open the output HTML file and refresh it after each run
# save(p)

## Generate <div> and <script> texts for other uses
script, div = components(p)
# print(div)
# print(script)
f = open("div.txt", "w")
f.write(div)
f.close()
f = open("script.txt", "w")
f.write(script)
f.close()
