from sqlalchemy import *

# Create database connection
def query(s, db):
    db = create_engine(db)
    conn = db.connect()
    result = conn.execute(s)
    return result

if __name__ == '__main__':
    # Query to select the police station coordinates
    def selectpolicecoords():
        result = query("SELECT longitude, latitude FROM police_stations", "sqlite:///data/Opendata.db")
        for i in result:
            print(i)

    # Query to select the burglary coordinates
    def selectroofcoords():
        result = query("SELECT longitude, latitude FROM Straatroven", "sqlite:///data/Opendata.db")
        for i in result:
            print(i)

    #selectpolicecoords()
    #selectroofcoords()