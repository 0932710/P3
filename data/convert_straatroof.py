import csv
import time
import pandas as pd
import re

class Straatroof:
    def __init__(self, voorval_nr, regdatum, maandnaam, gem_week, gem_datum, dagsoort, dagdeel, begindatum, begintijd, einddatum, eindtijd, plaats, straat ):
        self.voorval_nr = voorval_nr
        self.regdatum = regdatum
        self.maandnaam = maandnaam
        self.gem_week = gem_week
        self.gem_datum = gem_datum
        self.dagsoort = dagsoort
        self.dagdeel = dagdeel
        self.begindatum = begindatum
        self.begintijd = begintijd
        self.einddatum = einddatum
        self.eindtijd = eindtijd
        self.plaats = plaats
        self.straat = straat

    huisnummer = None
    toevoeging = None
    postcode = None
    soort_locatie = None
    poging_tot = None
    opgelost = None
    omgeving = None
    sexe_so = None
    leeftijdcat = None
    buit = None
    wapen = None
    wapen_soort = None
    wapen_naam = None
    letsel_so = None
    geweld = None
    activiteit = None
    omschrijving = None
    ddr_aantal = None
    voertuig = None
    voertuig_soort = None
    merk_gsm = None

    latitude = None
    longitude = None

    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())


def setCoords(straatroof_array, adres_csv):
    adres_dict = {"longitude": "LON", "latitude": "LAT", "huisnummer": "NUMBER", "straat": "STREET",
                  "plaats": "CITY", "postcode": "POSTCODE"}

    df = pd.read_csv(adres_csv, usecols=list(adres_dict.values()), encoding='utf-8')
    print("df loaded")

    df = df[(df[adres_dict["postcode"]].str[:2] == "30") | (df[adres_dict["postcode"]].str[:2] == "31")]
    print("postcodes cut")

    # df.to_csv("countrywide/nl/rotterdam3031.csv", encoding='utf-8')

    def addCoords(roof, row):
        if not row.empty:
            latitude = row.iloc[0][adres_dict["latitude"]]
            longitude = row.iloc[0][adres_dict["longitude"]]
            if (latitude is not None) and (longitude is not None):
                roof.latitude = latitude
                roof.longitude = longitude
                print("Coördinaten: ({0}, {1})".format(latitude, longitude))
            return True
        else:
            return False

    looptime = time.time()

    for roof in straatroof_array:
        print("Time: ", time.time() - looptime )
        looptime = time.time()

        latitude = None
        longitude = None

        first_pcode = None
        first_straat = None

        # Fail-safe monkey patching because of super weird error and i'm just really bad at programming
        for i, attribute in enumerate(adres_dict):
            if hasattr(roof, attribute):
                if i + 1 == len(adres_dict):
                    break
                continue
        else:
            continue

        # Get variables
        if roof.straat is not None:
            straat = re.sub("[(].*?[)]", "", roof.straat)
            if straat[-1] == " ":
                straat = straat[:-1]
        else: straat = None
        if roof.plaats is not None: plaats = str.title(roof.plaats)
        else: plaats = None
        if roof.huisnummer is not None: huisnummer = roof.huisnummer
        else: huisnummer = None
        if roof.toevoeging is not None: toevoeging = roof.toevoeging.upper()
        else: toevoeging = ""
        if roof.postcode is not None and len(roof.postcode) == 6: postcode = roof.postcode
        else: postcode = None

        print("----------------------")
        print(roof)
        # Decisiontree
        if postcode is not None: #When postcode is known
            row_pc = df[(df[adres_dict["postcode"]] == postcode)] #Narrow down search to postcode
            if huisnummer is not None:
                if toevoeging is not None:
                    print(roof.voorval_nr + "postcode + nr + toevoeging: " + postcode + huisnummer + toevoeging)
                    row = row_pc[row_pc[adres_dict["huisnummer"]] == huisnummer + toevoeging]
                    if addCoords(roof, row):
                        continue
                    if True:
                        print(roof.voorval_nr + "postcode + nr: " + postcode + huisnummer)
                        row = row_pc[row_pc[adres_dict["huisnummer"]] == huisnummer]
                        if addCoords(roof, row):
                            continue
            if True: #Get coords of postcode
                print(roof.voorval_nr + "postcode: " + postcode)
                addCoords(roof, row_pc)
                continue
        else:
            row_str = df[df[adres_dict["straat"]].str.upper() == straat]
            if huisnummer is not None:
                print(roof.voorval_nr + "straat + nr + toevoeging: " + straat + huisnummer + toevoeging)
                row = row_str[(row_str[adres_dict["huisnummer"]] == huisnummer + toevoeging)]
                if addCoords(roof, row):
                    continue
                else:
                    print(roof.voorval_nr + "straat + nr: " + straat + huisnummer)
                    row = row_str[(row_str[adres_dict["huisnummer"]] == huisnummer)]
                    if addCoords(roof, row):
                        continue
            if True:
                print(roof.voorval_nr + "straat: " + straat)
                addCoords(roof, row_str)
                continue

    return straatroof_array

def csvConvert(roof_csv):
    straatroof_array = []

    roof_dict = {0: 'voorval_nr', 1: 'regdatum', 2: 'maandnaam', 3: 'gem_week', 4: 'gem_datum', 5: 'dagsoort',
                 6: 'dagdeel', 8: 'begindatum', 9: 'begintijd', 10: 'einddatum', 11: 'eindtijd', 14: 'plaats',
                 19: 'straat', 20: 'huisnummer', 21: 'toevoeging', 22: 'postcode', 23: 'soort_locatie',
                 24: 'poging_tot', 25: 'opgelost', 27: 'omgeving', 28: 'sexe_so', 29: 'leeftijdcat', 30: 'buit',
                 31: 'wapen', 32: 'wapen_soort', 33: 'wapen_naam', 34: 'letsel_so', 35: 'geweld', 36: 'actviteit',
                 37: 'omschrijving', 38: 'ddr_aantal', 39: 'voertuig', 40: 'voertuig_soort'}
    last_init = 19
    plaats = "ROTTERDAM"

    with open(roof_csv, newline='', encoding='cp850' ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #, quotechar='|')
        for row in reader:
            case = ""
            case_args = {}

            if (not row[0][:-2].isnumeric()) and (not len(row[0]) == 12):
                continue
            if len(row) < last_init:
                continue
            if plaats not in row[14]:
                continue

            for nr in range(last_init + 1):
                if row[nr] is None or row[nr] == "":
                    break
            else:
                for nr in range(len(row)):
                    if (nr in roof_dict) and (row[nr] is not None and row[nr] != ""):
                        if nr <= last_init:
                            case_args[roof_dict[nr]] = row[nr]
                            if nr == last_init:
                                case = Straatroof(**case_args)
                        if nr > last_init:
                            if nr > max(roof_dict.keys(), key=int):
                                break
                            else:
                                setattr(case, roof_dict[nr], row[nr])
            straatroof_array.append(case)
    print("Alle roven zijn geschraapt!")
    return straatroof_array

def straatroofConverter(roof_csv, adres_csv):
    straatroof_array = csvConvert(roof_csv)
    return setCoords(straatroof_array, adres_csv)



if __name__ == '__main__':
    roof_csv = 'straatroof-2011.csv'
    adres_csv = 'countrywide/nl/countrywide.csv'
    #adres_csv = 'countrywide/nl/rotterdam3031.csv'

    def test1():
        start = time.time()
        roof_array = straatroofConverter(roof_csv, adres_csv)
        print(len(roof_array))
        print("total time taken this loop: ", time.time() - start)

    test1()