from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Server</h1>"

lst_users = ["Admin","Jake","Tim","Eric"]

@app.route("/<name>")
def user_page(name):
    return render_template("index.html",content=lst_users)

if __name__ == "__main__":
    app.run()