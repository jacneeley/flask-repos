from flask import Blueprint, render_template
import server.config
from server.config import db

blueprint_home = Blueprint("home_page", __name__, static_folder="static", static_url_path='/static/styles/' ,template_folder="templates/home.html")

@blueprint_home.route("/home")
@blueprint_home.route("/")
def render_home():
    return render_template("home.html",data =db)