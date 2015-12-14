from bokeh.io import output_notebook, show
from bokeh.plotting import figure
import requests, simplejson
import pandas as pd
import web

    
stock='FB'
r=requests.get('https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=tX-ANP6Rh24Q81bFsYH5',stock)
df = pd.read_json('https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=tX-ANP6Rh24Q81bFsYH5')
df = pd.DataFrame(df['dataset']['data'])

# set up some data
x=pd.to_datetime(pd.Series(df[0]))
x=x.tolist()
y = df[1].tolist()

output_notebook()

# create a new plot with figure
p = figure(plot_width=800, plot_height=800, x_axis_type='datetime',title='Ticker Data',
              x_axis_label='date', y_axis_label='price')

# add both a line and circles on the same plot
p.line(x,y, line_width=2)

#output_file("scatter.html")

show(p) # show the results