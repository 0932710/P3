from sqlalchemy import *

def query(parameter):
    db = create_engine('sqlite:///Opendata.db')
    s = (parameter)
    conn = db.connect()
    return conn.execute(s)

if __name__ == '__main__':
    result = query("SELECT * FROM Straatroven")

    for i in result:
        print(i)