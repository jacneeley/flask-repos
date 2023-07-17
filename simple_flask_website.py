from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page <h1>Welcome to my flask site!</h1>"

@app.route("/<name>") #input a paramter into url to pass into function
def user(name):
    return f"Hello {name}!"

#return redirect from a specific function
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()