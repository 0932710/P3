from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload")
def maps():
  return render_template("upload.html")

@app.route("/css")
def css():
  return render_template("test.css")

app.run()
