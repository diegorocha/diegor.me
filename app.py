from flask import Flask, render_template, redirect, abort
import diegor_me

app = Flask(__name__)

@app.route("/")
def index():
    return handle_alias()

@app.route("/<alias>")
def alias_url(alias):
    return handle_alias(alias)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.htm"), 404

def handle_alias(alias=''):
    url = diegor_me.get_url_from_alias(alias)
    if url:
       return redirect(url, code=302)
    else:
       abort(404)

app.run()
