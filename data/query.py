from sqlalchemy import *

def query(s, db):
    db = create_engine(db)
    conn = db.connect()
    result = conn.execute(s)
    return result

if __name__ == '__main__':
    def selectpolicecoords():
        result = query("SELECT longitude, latitude FROM police_stations", 'sqlite:///Opendata.db')
        for i in result:
            print(i)

    def selectroofcoords():
        result = query("SELECT voorval_nr, longitude, latitude FROM Straatroven", 'sqlite:///Opendata.db')
        for i in result:
            print(i)

    #selectpolicecoords()
    selectroofcoords()