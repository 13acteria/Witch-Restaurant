from flask import Flask
from flask import request
from flask import render_template

app = Flask(
    __name__,
    static_folder='gallery',
    static_url_path='/g/')

login_status = 'no'
login_account = 'Ayame'
historyData = '2,1,2,3,4,5,6'
recommandData = '2,1,2,3,4,5,6,7,8,8,7,6,5,4,3,2,1'
# ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData

@app.route('/')
def index():
    return render_template('home.html' ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData)

@app.route('/map')
def map_handle():
    return render_template('map.html' ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData)

@app.route('/record')
def record_handle():
    return render_template('record.html' ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData)

@app.route('/recommand')
def rcd_handle():
    return render_template('recommand.html' ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData)

@app.route('/account')
def account_handle():
    return render_template('account.html' ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData)

@app.route('/login')
def login_handle():
    login_status = 'yes'
    return render_template('home.html' ,login_status=login_status, login_account=login_account, historyData=historyData, recommandData=recommandData)

# @app.route('/arg/')
# def get_arg():
#     arg1 = request.args.get('arg1', 0)
#     arg2 = request.args.get('arg2', 0)
#     arg1, arg2 = int(arg1), int(arg2)
#     return 'sum: '+str(arg1+arg2)

if __name__ == '__main__':
    app.run()