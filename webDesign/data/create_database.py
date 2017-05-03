from sqlalchemy import *
import datetime

#The code below defines and creates a connection to the table police_stations
def politiesql(stations):
    db = create_engine('sqlite:///Opendata.db')
    db.echo = True  # Try changing this to True and see what happens
    metadata = MetaData(db)
    #The code below defines the table format with the corresponding datatypes
    Politie = Table('police_stations', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('naam', String(40)),
                    Column('adres', String(40)),
                    Column('latitude', Float),
                    Column('longitude', Float),
                    )

    d = Politie.delete()
    d.execute()

    i = Politie.insert()
    
    for station in stations: #This statement provides the right information to inject the data
        i.execute(naam=station.naam, adres=station.adres, latitude=station.latitude, longitude=station.longitude)

def straatroofsql(roofovervallen):
    db = create_engine('sqlite:///Opendata.db')
    db.echo = True #gives debugging information at execution
    metadata = MetaData(db)
    # The code below defines and creates a connection to the table straat_roven
    Straatroof = Table('Straatroven', metadata,
                       Column('voorval_nr', String(20), primary_key=True),
                       Column('regdatum', Date),
                       Column('maandnaam', String(80)),
                       Column('gem_week', String(80)),
                       Column('gem_datum', Date),
                       Column('dagsoort', String(80)),
                       Column('dagdeel', String(25)),
                       Column('begindatum', Date),
                       Column('begintijd', Date),
                       Column('einddatum', Date),
                       Column('eindtijd', Date),
                       Column('plaats', String(30)),
                       Column('straat', String(30)),
                       Column('huisnummer', Integer),
                       Column('toevoeging', String(10)),
                       Column('postcode', String(6)),
                       Column('soort_locatie', String(20)),
                       Column('poging_tot', String(40)),
                       Column('opgelost', String(6)),
                       Column('omgeving', String(60)),
                       Column('sexe_so', String(10)),
                       Column('leeftijdcat', String(30)),
                       Column('buit', String(80)),
                       Column('wapen', String(40)),
                       Column('wapen_soort', String(25)),
                       Column('wapen_naam', String(30)),
                       Column('letsel_so', String(100)),
                       Column('geweld', String(40)),
                       Column('activiteit', String(80)),
                       Column('omschrijving', String(200)),
                       Column('ddr_aantal', String(10)),
                       Column('voertuig', String(30)),
                       Column('voertuig_soort', String(20)),
                       Column('merk_gsm', String(20)),
                       Column('latitude', Float),
                       Column('longitude', Float)
                       )
    d = Straatroof.delete()
    d.execute()

    i = Straatroof.insert()

    print("Amount of overvallen: " )
    breaknr = 0
    loopnr = 0

    for roof in roofovervallen:
        print(roof)
        loopnr += 1

        if not hasattr(roof, 'voorval_nr'): #safe-fail
            breaknr += 1
            continue
        #The code below gives the right table formating for executing the SQL query
        i.execute(voorval_nr=roof.voorval_nr,
                  regdatum=datetime.datetime.strptime(roof.regdatum, '%d/%m/%Y'),
                  maandnaam=roof.maandnaam,
                  gem_week=roof.gem_week,
                  gem_datum=datetime.datetime.strptime(roof.gem_datum, '%d/%m/%Y'),
                  dagsoort=roof.dagsoort,
                  dagdeel=roof.dagdeel,
                  begindatum=datetime.datetime.strptime(roof.begindatum, '%d/%m/%Y'),
                  begintijd=datetime.datetime.strptime(roof.begintijd, '%H:%M'),
                  einddatum=datetime.datetime.strptime(roof.einddatum, '%d/%m/%Y'),
                  eindtijd=datetime.datetime.strptime(roof.eindtijd, '%H:%M'),
                  plaats=roof.plaats,
                  straat=roof.straat,
                  huisnummer=roof.huisnummer,
                  toevoeging=roof.toevoeging,
                  postcode=roof.postcode,
                  soort_locatie=roof.soort_locatie,
                  poging_tot=roof.poging_tot,
                  opgelost=roof.opgelost,
                  omgeving=roof.omgeving,
                  sexe_so=roof.sexe_so,
                  leeftijdcat=roof.leeftijdcat,
                  buit=roof.buit,
                  wapen=roof.wapen,
                  wapen_soort=roof.wapen_soort,
                  wapen_naam=roof.wapen_naam,
                  letsel_so=roof.letsel_so,
                  geweld=roof.geweld,
                  activiteit=roof.activiteit,
                  omschrijving=roof.omschrijving,
                  ddr_aantal=roof.ddr_aantal,
                  voertuig=roof.voertuig,
                  voertuig_soort=roof.voertuig_soort,
                  merk_gsm=roof.merk_gsm,
                  latitude=roof.latitude,
                  longitude=roof.longitude
                  )

    print("This many breaks: ", breaknr)
    print("This many loops: ", loopnr)

if __name__ == '__main__':
    from convert_politie import *
    from convert_straatroof import *
    def politie(): #function for calling and execution of sql statements for the table police_stations
        xml = 'bureaus.xml'
        stations = xmlConvert(xml)
        politiesql(stations)

    def straatroofFull(): #function for calling and execution of sql statements for the table straatroven
        roof_csv = 'straatroof-2011.csv'
        adres_csv = 'rotterdam3031.csv'
        roof_array = straatroofConverter(roof_csv, adres_csv)
        print("Amount of overvallen: ", len(roof_array))
        straatroofsql(roof_array)

    def straatroof(): # testfunction with dummiedata
        roofje = Straatroof('22233423534534523', '11/12/2012', 'November', '52', '11/12/2011', 'Woensdag', 'ochtend', '22/10/1993', '12:30', '11/11/2011', '22:20', 'ROTTERDAM', 'Coolsingel')
        roofje_array = {roofje}
        straatroofsql(roofje_array)

    straatroofFull()
