from geopy.distance import vincenty
from query import *

def add_distance():
    roofq = query("SELECT voorval_nr, latitude, longitude FROM Straatroven")

    db = create_engine('sqlite:///Opendata.db')
    db.echo = True  # Try changing this to True and see what happens
    metadata = MetaData(db)

    db.connect()

    Straatroof = Table('Straatroven', metadata,
                       Column('voorval_nr', String(20), primary_key=True),
                       Column('distance_pol', Float))

    u = Straatroof.update()


    distancearray = []

    for r in roofq: #brace yourself for the dumbest piece of code ever, but hey, it works
        voorval_nr = r['voorval_nr']
        print(voorval_nr)
        rpoint = (r['latitude'], r['longitude'])
        distance = None
        policeq = query("SELECT latitude, longitude FROM police_stations")
        for p in policeq:
            ppoint = (p['latitude'], p['longitude'])
            if distance is None:
                distance = vincenty(rpoint, ppoint).meters
            elif distance > vincenty(rpoint, ppoint).meters:
                distance = vincenty(rpoint, ppoint).meters
        if distance > 10000:
            distance = None
        distancearray.append([voorval_nr, distance])

    print(distancearray)

    for i in distancearray:
        u2 = u.where(Straatroof.c.voorval_nr == i[0]).values(distance_pol=i[1])
        u2.execute()


if __name__ == '__main__':
    add_distance()