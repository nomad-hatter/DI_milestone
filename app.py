from flask import Flask, render_template, request, redirect
from bokeh.io import output_notebook, show
from pandas import DataFrame
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components

app = Flask(__name__)
app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
    
    if request.method == 'GET':
          return render_template('index.html')

    else:
    
        app.vars['ticker']=request.form['ticker']
        
        api_url='https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=tX-ANP6Rh24Q81bFsYH5'%(app.vars['ticker'])

        df = pandas.read_json(api_url)
        df = pandas.DataFrame(df['dataset']['data'])
        
        # set up some data
        x=pandas.to_datetime(pd.Series(df[0]))
        x=x.tolist()
        y = df[1].tolist()
        
        #output_notebook()
        
        # create a new plot with figure
        #p = figure(plot_width=800, plot_height=800, x_axis_type='datetime',title='Ticker Data',x_axis_label='date', y_axis_label='price')

        # add both a line and circles on the same plot
        #p.line(x,y, line_width=2)

        #output_file("graph.html")
        #show(p) # show the results
        #from bokeh.embed import components 

        #script, div = components(p)
        return '%s'%(app.vars['ticker'])
        #return '%s'%y
        #return render_template('graph.html', script=script, div=div)
        #return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)

