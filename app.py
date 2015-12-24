from flask import Flask, render_template, redirect, abort
import diegor_me

app = Flask(__name__)

@app.route("/")
def index():
    return handle_alias()

@app.route("/<alias>")
def alias_url(alias):
    return handle_alias(alias)

@app.route("/add")
def add():
    return render_template("add.htm")

@app.route("/save")
def save():
    item = {'alias': None, 'url': None}
    if diegor_me.save(item):
	return render_template("saved.htm")
    return render_template("error.htm")

@app.errorhandler(404)
def not_found(error):
    return render_template("404.htm"), 404

def handle_alias(alias=''):
    url = diegor_me.get_url_from_alias(alias)
    if url:
       return redirect(url, code=302)
    else:
       abort(404)

if __name__ == '__main__':
    app.run()
