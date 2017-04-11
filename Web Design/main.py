from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload")
def maps():
  return render_template("upload.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/css")
def css():
  return render_template("style.css")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
