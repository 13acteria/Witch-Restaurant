from flask import Flask
from flask import request
from flask import render_template
#hi
app = Flask(
    __name__,
    static_folder='gallery',
    static_url_path='/g/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return 'my data'

@app.route('/user/<username>')
def user(username):
    return 'Hello '+username

@app.route('/arg/')
def get_arg():
    arg1 = request.args.get('arg1', 0)
    arg2 = request.args.get('arg2', 0)
    arg1, arg2 = int(arg1), int(arg2)
    return 'sum: '+str(arg1+arg2)

app.run(port=4000)