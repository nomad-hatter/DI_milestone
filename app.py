from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['POST'])
def index():
    if request.method == 'POST':
        app.vars['ticker']=request.form['ticker']
         f = open('%s.txt'%(app.vars['ticker']),'w')
         f.write('%s\n'%(app.vars['ticker']))
         f.close()
    else:
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)

