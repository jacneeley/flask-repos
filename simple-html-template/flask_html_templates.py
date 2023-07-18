from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__,template_folder='templates', static_folder='static')
app.secret_key = "supersecret"
app.permanent_session_lifetime = timedelta(minutes=5)

session

@app.route("/")
def home():
    return render_template("welcome.html")

lst_users = ["Admin","Jake","Tim","Eric"]

@app.route("/owners")
def owners_page():
    user = session["user"]
    return render_template("index.html",owners=lst_users, activeUser = user)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["inputName"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user")
def user():
    #get session info
    if "user" in session:
        user=session["user"]
        return redirect(url_for("owners_page"))
    else:
        #redirect
        return redirect(url_for("login.html"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)