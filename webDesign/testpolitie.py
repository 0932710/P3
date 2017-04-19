from data.query import *

def politie_map():
    coordslist = []
    pmapsql = query(
        "SELECT latitude, longitude "
        "FROM police_stations",
        "sqlite:///data/Opendata.db")
    for i in pmapsql:
        if (i.latitude is None) or (i.longitude is None):
            continue
        coordslist.append([i.latitude, i.longitude])
    return coordslist

print(politie_map())
