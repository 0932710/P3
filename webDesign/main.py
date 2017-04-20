from flask import Flask, render_template
from data.query import *

app = Flask(__name__)

# Function to query the latitude and longitude coordinates of all burglaries in Rotterdam
def map():
    # Create an empty list to store the coordinates in
    latlong = []
    # Assign the query to a variable
    mapsql = query(
        "SELECT latitude, longitude "
        "FROM Straatroven",
        "sqlite:///data/Opendata.db")
    for i in mapsql:
        # Skip the row if either the latitude or longitude coordinates are 'None'/missing
        if (i.latitude is None) or (i.longitude is None):
            continue
        # Add the coordinates to the dictionary
        dict = {'lat': i.latitude, 'lng': i.longitude}
        # Append the dictionary to the (initially empty) latlong list
        latlong.append(dict)
    # Assign the latlong list to the data propery
    retDict = {'data': latlong}
    return retDict

# Function to query the latitude and longitude coordinates of all police stations in Rotterdam
def politie_map():
    coordslist = []
    pmapsql = query(
        "SELECT latitude, longitude, naam "
        "FROM police_stations",
        "sqlite:///data/Opendata.db")
    for i in pmapsql:   
        if (i.latitude is None) or (i.longitude is None):
            continue
        coordslist.append([i.latitude, i.longitude, i.naam])
    return coordslist


def plot1():
    # Query to obtain the required information for the first plot
    plot1sql = query(
        "SELECT strftime('%Y', begindatum) AS jaar, strftime('%m', begindatum) AS maand, maandnaam, count(*) AS count_1 "
        "FROM(SELECT begindatum, maandnaam"
        "     FROM Straatroven)"
        "GROUP BY jaar, maand",
        "sqlite:///data/Opendata.db"
    )
    # Create an empty list
    list_dict = []
    for i in plot1sql:
        # Add the SQL results to a dictionary
        dict = {'date': i.maandnaam + "-" + i.jaar, 'value': i.count_1}
        # Append the dictionary to the (initially empty) list_dict list
        list_dict.append(dict)
    # Return the list for further use in the application
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

# Underneath code is used to tell the application where each page can be found, document root will return index.html
@app.route("/")
def index():
    return render_template("index.html", plot1_json = plot1(), plot2_json = plot2(), map_roofdata = map(), map_politiedata = politie_map())


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