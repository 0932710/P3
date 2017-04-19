from flask import Flask, render_template
from data.query import *

app = Flask(__name__)

def map():
    maps

def plot1():
    plot1sql = query(
        "SELECT strftime('%Y', begindatum) AS jaar, strftime('%m', begindatum) AS maand, maandnaam, count(*) AS count_1 "
        "FROM(SELECT begindatum, maandnaam"
        "     FROM Straatroven)"
        "GROUP BY jaar, maand",
        'sqlite:///data/Opendata.db')

    list_dict = []
    for i in plot1sql:
        dict = {'date': i.maandnaam + "-" + i.jaar, 'value': i.count_1}
        list_dict.append(dict)

    return list_dict

def plot2():
    list_dict = []

    dLast = 0
    d = 50
    while d <= 3000:
        plot2sql = query(
            "SELECT count(*) AS count_1 "
            "FROM Straatroven "
            "WHERE distance_pol > {0} AND distance_pol < {1}".format(dLast, d),
            "sqlite:///data/Opendata.db"
        )
        for i in plot2sql:
            print(d, i.count_1)
            dict = {'date': str(dLast) + "-" + str(d), 'value': i.count_1}
            list_dict.append(dict)
        dLast = d
        d = d + 50

    return list_dict

@app.route("/")
def index():
    return render_template("index.html", plot1_json = plot1(), plot2_json = plot2())

@app.route("/upload")
def maps():
  return render_template("upload.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/css")
def css():
  return render_template("style.css")

if __name__=="__main__":
  app.run(host="0.0.0.0")