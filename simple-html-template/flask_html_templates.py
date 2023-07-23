from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import select



app = Flask(__name__,template_folder='templates', static_folder='static')
app.secret_key = "supersecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)
class users(db.Model):
    id = db.Column("id",db.Integer, primary_key=True)
    email = db.Column("Email",db.String(100))
    username = db.Column("Username",db.String(100))
    password = db.Column("Userpassword",db.String(50))

    def __init__(this,email,username,password):
        this.email = email
        this.username = username
        this.password = password

session

@app.route("/")
def home():
    return render_template("welcome.html")

lst_users = ["Admin","Jake","Tim","Eric"]

@app.route("/owners")
def owners_page():
    if "activeUser" in session:
        user = session["activeUser"]
        return render_template("index.html",owners=lst_users)
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["inputUsername"]
        session["activeUser"] = username
        found_user = db.session.query(users.id).filter_by(username=username).first()

        if found_user:
            # session["email"] = found_user.email
            # session["username"] = found_user.username
            # session["password"] = found_user.password
            return redirect(url_for("user"))
        else:
            session.pop("activeUser",None)
            flash("User does not exist...", "info")
            return render_template("login.html")
        
    else:
        if "activeUser" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route("/create", methods=["POST","GET"])
def create_user():
    #get session info
    email = None
    username = None
    password = None

    if request.method == "POST":
        username = request.form["inputUsername"]
        session["activeUser"] = username
        found_user = db.session.query(users.id).filter_by(username=username).first()

        if found_user:
            flash("User already exists...", "info")
            session.pop("activeUser", None)
            return render_template("create.html")
        else:
            email = request.form["inputEmail"]
            username = request.form["inputUsername"]
            password = request.form["inputPassword"]
            session["username"] = username
            newuser = users(email,username,password)
            db.session.add(newuser)
            db.session.commit()
            flash("Account Successfully created!", "info")
            return render_template("user.html",activeUser = username)
            
    else: 
        #method == "GET"
        if "username" in session:
            username = session["username"]
            flash("you must log out before creating a new account...","info")
            return render_template("user.html",activeUser = username)
        else: 
            return render_template("create.html")

@app.route("/user", methods=["POST","GET"])
def user():
    #get session info
    email = None
    username = None
    password = None
    
    if "activeUser" in session:
        username=session["activeUser"]
        ##update
        if request.method == "POST":
            email = request.form["inputEmail"]
            username = request.form["inputUsername"]
            password = request.form["inputPassword"]
            # session["email"] = email
            session["username"] = username
            # session["password"] = password
            found_user = db.session.query(users.id).filter_by(username=username).first()
            found_user.email = email
            found_user.username = username
            found_user.password = password
            db.session.commit()
        
        else: 
            if "username" in session:
                # email = session["email"]
                username = session["username"]
                # password = session["inputPassword"]
        return render_template("user.html",activeUser = username)
    
    else:
        #redirect #method == "GET"
        return redirect(url_for("login"))

@app.route("/userdb")
def view_users():
    if "activeUser" in session:
        return render_template("userdb.html", values = users.query.all())
    else:
        return redirect(url_for("login"))

@app.route("/deleteuser/<int:user_id>", methods=["POST"])
def del_users(user_id):
    if request.method == "POST":
        if "activeUser" in session:
            users.query.filter(users.id == user_id).delete()
            db.session.commit()
            flash('Item deleted.',"info")
            return redirect(url_for("view_users"))
        else:
            return redirect(url_for("login"))
    else:
        flash("ERROR", 'error')
        return redirect(url_for("view_users"))
    
@app.route("/logout")
def logout():
    if "activeUser" in session:
        flash("Successfully Logged Out", "info")
        session.pop("activeUser", None)
        session.pop("email", None)
        session.pop("username", None)
        session.pop("password", None)
        return redirect(url_for("home"))
    else:
        flash("You must login first...", "info")
        return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)