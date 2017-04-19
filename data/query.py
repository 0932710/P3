from sqlalchemy import *


def query(s):
    db = create_engine('sqlite:///Opendata.db')
    conn = db.connect()
    result = conn.execute(s)
    return result


if __name__ == '__main__':
    def selectpolicecoords():
        result = query("SELECT latitude, longitude FROM police_stations")
        for i in result:
            print(i)

    def selectroofcoords():
        result = query("SELECT latitude, longitude FROM Straatroven")
        resultl = []

        for i in result:
            resultl.append(i)

        resultDict = {}
        resultList = []
        testData = {}

        for x in range(len(resultl)):
            resultDict["lat"] = resultl[x][0]
            resultDict["lng"] = resultl[x][1]
            resultList.append(resultDict)

        testData["data"] = resultList

        straatrovenData = open("straatrovenData.txt", "w")
        straatrovenData.write(str(testData))
        straatrovenData.close()

    # selectpolicecoords()
    selectroofcoords()
