from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'JWT Auth tutorial'

if __name__ == '__main___':
    app.run(debug=True)