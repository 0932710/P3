from convert_politie import *
from convert_straatroof import *
from create_database import *

def politie(xml):
    #xml = 'bureaus.xml'
    stations = xmlConvert(xml)
    politiesql(stations)


def straatroof(roof_csv, adres_csv):
    #roof_csv = 'straatroof-2011.csv'
    #adres_csv = 'countrywide/nl/countrywide.csv'
    roof_array = straatroofConverter(roof_csv, adres_csv)
    straatroofsql(roof_array)

politie('bureaus.xml')
straatroof('straatroof-2011.csv', 'rotterdam3031.csv')