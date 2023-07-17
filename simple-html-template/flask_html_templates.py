from flask import Flask, redirect, url_for, render_template

app = Flask(__name__,template_folder='templates', static_folder='static')

# @app.route("/")
# def home():
#     return "<h1>Welcome to the Server</h1>"

lst_users = ["Admin","Jake","Tim","Eric"]

@app.route("/")
def index():
    return render_template("index.html",content=lst_users)

if __name__ == "__main__":
    app.run(debug=True)