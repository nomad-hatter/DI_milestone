from flask import Flask, render_template, request, redirect, url_for, flash
from bokeh.io import output_notebook, show
from pandas import DataFrame
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components
import pandas as pd
import time

app = Flask(__name__)
app.var={}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')

    else:
        return redirect(url_for('graph'))


@app.route('/graph',methods=['GET','POST'])
def graph():
    crnt_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    start_date = time.strftime('%Y-%m-%d',time.localtime(time.time()-60*60*24*28))

    symbol=request.form['ticker']
    option=request.form['option']

    symbol=symbol.upper()

    api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/'+symbol+'.json?start_date=' + start_date + '&end_date=' + crnt_date + '&column_index='+ option +'?api_key=tX-ANP6Rh24Q81bFsYH5l'
    try:
        df = pd.read_json(api_url)
    except:
        return redirect(url_for('index'))

    plotTitle=symbol+' '+df['dataset']['column_names'][1]+' Data'
    df = pd.DataFrame(df['dataset']['data'])

    # set up some data
    x=pd.to_datetime(pd.Series(df[0]))
    x=x.tolist()
    y = df[1].tolist()

    # create a new plot with figure
    p = figure(plot_width=800, plot_height=500, x_axis_type='datetime',title=plotTitle,x_axis_label='Date', y_axis_label='Price')

    p.line(x,y, line_width=2)

    script, div = components(p)

    return render_template('graph.html',script=script, div=div, symbol=symbol) 

if __name__ == '__main__':
    app.run(port=33507)
