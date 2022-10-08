## `figure` to create plots
## `output_file` to name the HTML file to generate
## 'show' to generate and output HTML files
from turtle import right
from bokeh.plotting import figure, output_file, show
import pandas as pd

## Data
# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]
## Read in CSV data file with Pandas
df = pd.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']

## Name the output HTML file
output_file('index.html')

## Add a plot
p = figure(
	y_range=car,
	plot_width=800,
	plot_height=600,
	title = 'Cars with Top Horsepower',
	x_axis_label = 'Horsepower',
	# y_axis_label = 'Y Axis',
	## No tool displayed
	tools=''
)

## Render glyph
## Add a line graph
# p.line(x, y, legend='Test', line_width=2)
## Add a horizontal bar chart
p.hbar(
	y=car,
	right=hp,
	left=0,
	height=0.4,
	color='green',
	fill_alpha=0.5
	)

## Show the plot
show(p)
