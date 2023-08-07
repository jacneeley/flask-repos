from flask import Blueprint, render_template
import server.config
from server.config import db

get_db_imgs = Blueprint("get_imgs", __name__, static_folder="static", static_url_path='/static/styles/' ,template_folder="templates")

@get_db_imgs.route("/home")
@get_db_imgs.route("/")
def home():
    return render_template("home.html",data =db)