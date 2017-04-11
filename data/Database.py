from sqlalchemy import *

db = create_engine('sqlite:///Opendata.db')

db.echo = True  # Try changing this to True and see what happens

metadata = MetaData(db)

Politie = Table('police_stations', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('address', String(40)),
    Column('latitude', Float),
    Column('longitude', Float),
)


i = Politie.insert()
i.execute(name='Rotterdam', address='kalmoestraat 37', latitude=3.4657, longitude=2.3434)
i.execute({'name': 'Schieweg', 'address': 'alsemstr 23', 'long': 3.4322, 'lat': 2.3456},
          {'name': 'Schiweer', 'address': 'halsemstr 23', 'long': 3.4322, 'lat': 2.3456},
          {'name': 'Schiederweg', 'address': 'balsemstr 26', 'long': 3.4332, 'lat': 2.34536})

s = Politie.select()
rs = s.execute()

