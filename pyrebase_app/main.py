from flask import Flask, render_template
from server.get_imgs import get_db_imgs

app = Flask(__name__, static_folder="server/static/")
app.register_blueprint(get_db_imgs, url_prefix="/server")
@app.route("/")
def test():
    return "<h1>Test Landing Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)