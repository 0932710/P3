# coding=utf-8
import xml.etree.ElementTree as ET

class Bureau:
    def __init__(self, naam, adres, lat, lng):
        self.naam = naam
        self.adres = adres
        self.latitude = lat
        self.longitude = lng

    def __str__(self):
        return "Bureau: {0}\n Adres: {1}\n Coördinaten: ({2}, {3})"\
            .format(self.naam, self.adres, self.latitude, self.longitude)


def xmlConvert(file):
    tree = ET.parse(file)
    root = tree.getroot()

    sv = str.replace(root.tag,'node','')
    cities = ['Rotterdam']

    stations = []

    for city in cities:
        stations_cty = root.findall(
            ".//*[@{0}name='politiemaps:administrative_area_level_2']/[{0}value='{1}']../.."
                .format(sv, city)
        )
        for i in stations_cty:
            stations.append(i)

    station_array = []
    #print(stations)

    for station in stations:
        #print(station.attrib['{0}name'.format(sv)])
        name = station.find("./*[@{0}name='politie:titel']/[{0}value]".format(sv))[0].text
        location = station.findall(".//*[@{0}name='politiemaps:points']".format(sv))[0][0].text
        location = location.split(",")
        lat = location[0]
        lng = location[1]
        address = location[2]

        station_array.append(Bureau(name, address, lat, lng))

    return station_array


if __name__ == '__main__':
    xml = 'bureaus.xml'
    station_array = xmlConvert(xml)
    i = 0
    for station in station_array:
        i += 1
        print(station)
    print(i)