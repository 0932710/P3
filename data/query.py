from sqlalchemy import *

def query(s, db):
    db = create_engine(db)
    conn = db.connect()
    result = conn.execute(s)
    return result


if __name__ == '__main__':
    def selectpolicecoords():
        result = query("SELECT latitude, longitude FROM police_stations", 'sqlite:///Opendata.db')
        resultl = []
        for i in result:
            resultl.append(i)

        resultDict = {}
        resultList = "["
        politieData = "{'data': "

        for x in range(len(resultl)):
            resultDict["lat"] = resultl[x][0]
            resultDict["lng"] = resultl[x][1]
            if resultDict["lat"] != None or resultDict["lng"] != None:
                resultList = resultList + str(resultDict)
                if x < len(resultl) - 1:
                    resultList = resultList + ", "

        resultList = resultList + "]"
        politieData = politieData + resultList
        politieData = politieData + "}"

        politieData = open("../webDesign/static/leaflet/politieData.js", "w")
        politieData


    def selectroofcoords():
        result = query("SELECT latitude, longitude FROM Straatroven", 'sqlite:///Opendata.db')
        resultl = []
        for i in result:
            resultl.append(i)

        resultDict = {}
        resultList = "["
        roofData = "{'data': "

        for x in range(len(resultl)):
            resultDict["lat"] = resultl[x][0]
            resultDict["lng"] = resultl[x][1]
            if resultDict["lat"] != None or resultDict["lng"] != None:
                resultList = resultList + str(resultDict)
                if x < len(resultl) - 1:
                    resultList = resultList + ", "

        resultList = resultList + "]" 

        roofData = roofData + resultList
        roofData = roofData + "}"

        straatrovenData = open("../webDesign/static/leaflet/straatrovenData.js", "w")
        straatrovenData.write("var testData = " + str(roofData))
        straatrovenData.close()

    # selectpolicecoords()
    selectroofcoords()
