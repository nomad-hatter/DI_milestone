from flask import Flask, render_template, request, redirect, url_for
from bokeh.io import output_notebook, show
from pandas import DataFrame
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components
import pandas as pd
import time

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
        
    if request.method == 'GET':
          return render_template('index.html')

    else:
    
        #app.vars['ticker']=request.form['ticker']
        #symbol=request.form['ticker']
        #session['symbol']=request.form['ticker']
        return redirect(render_template('graph',symbol=request.form['ticker']))

@app.route('/graph',methods=['GET','POST'])
def graph():
        
        crnt_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        start_date = time.strftime('%Y-%m-%d',time.localtime(time.time()-60*60*24*31))
        
        #symbol=request.args['symbol']
        #api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'.json?start_date=' + start_date + '&end_date=' + crnt_date + '?api_key=tX-ANP6Rh24Q81bFsYH5l'
    
        #df = pd.read_json(api_url)
        #df = pd.DataFrame(df['dataset']['data'])
        
        # set up some data
        #x=pd.to_datetime(pd.Series(df[0]))
        #x=x.tolist()
        #y = df[1].tolist()
          
        # create a new plot with figure
        #p = figure(plot_width=400, plot_height=400, x_axis_type='datetime',title='Ticker Data',x_axis_label='date', y_axis_label='price')

        #p.line(x,y, line_width=2)

        #resources = RESOURCES.render(js_raw=INLINE.js_raw,css_raw=INLINE.css_raw,js_files=INLINE.js_files,css_files=INLINE.css_files,)

        #script, div = components(p)

        #return render_template('graph.html',script=script, div=div) 
        return 'test %s'%(symbol)
    
if __name__ == '__main__':
    app.run(port=33507)
