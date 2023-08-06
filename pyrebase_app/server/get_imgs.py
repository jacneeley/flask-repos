from flask import Blueprint, render_template
import server.config
from server.config import db

get_imgs = Blueprint("get_imgs", __name__, static_folder="static", template_folder="templates")

@get_imgs.route("/home")
@get_imgs.route("/")
def home():
    return render_template("home.html",data =db)