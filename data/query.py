from sqlalchemy import *

def query(s):
    db = create_engine('sqlite:///Opendata.db')
    conn = db.connect()
    return conn.execute(s)

if __name__ == '__main__':
    def selectpolicecoords():
        result = query("SELECT longitude, latitude FROM police_stations")
        for i in result:
            print(i)

    def selectroofcoords():
        result = query("SELECT longitude, latitude FROM Straatroven")
        for i in result:
            print(i)

    #selectpolicecoords()
    selectroofcoords()