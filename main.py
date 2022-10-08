## `figure` to create plots 
## `output_file` to name the HTML file to generate
## 'show' to generate and output HTML files 
from bokeh.plotting import figure, output_file, show 

## Data 
x = [1, 2, 3, 4, 5]
y = [4, 6, 2, 4, 3]

## Name the output HTML file
output_file('index.html')

## Add a plot 
p = figure(
	title = 'Bokeh Line Graph Test', 
	x_axis_label = 'X Axis', 
	y_axis_label = 'Y Axis'
)

## Render glyph
## Add a line graph
p.line(x, y, legend='Test', line_width=2)

## Show the plot
show(p)
