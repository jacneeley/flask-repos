from flask import Flask , request, jsonify, session, render_template, flash, make_response
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Demonstration'

def check_token(func):
    ##decline access if user doesn't have the correct jwt
    @wraps(func)
    def wrapped(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({"Message":"Missing Token"}),403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({"Message": "Invalid Token"}), 403
        return func(*args,**kwargs)
    return wrapped

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Currently logged in.'
    
@app.route('/public')
def public():
    return 'Public View.'

@app.route('/auth')
@check_token
def authorised():
    return "congrats, your token is valid!"

@app.route('/login',methods=['POST'])
def login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['logged_in'] = True
        token = jwt.encode({
            'user' : request.form['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
        },
        app.config['SECRET_KEY'])
        return jsonify({'token' : token})
    else:
        return make_response('unable to verify', 403, {'WWW-Authenticate' : 'Basic realm: "login.'})

if __name__ == '__main__':
    app.run(debug=True)