from data.query import *

""""
def plot2():
    list_dict = []

    dLast = 0
    d = 50
    while d <= 3000:
        plot2sql = query(
            "SELECT count(*) AS count_1 "
            "FROM Straatroven "
            "WHERE distance_pol > {0} AND distance_pol < {1}".format(dLast, d),
            "sqlite:///data/Opendata.db"
        )
        for i in plot2sql:
            print(d, i.count_1)
            dict = {'afstand': dLast + "-" + d, 'value': i.count_1}
            list_dict.append(dict)
        dLast = d
        d = d + 50

    return list_dict
"""
