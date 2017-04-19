from data.query import *


plot1sql = query(
    "SELECT strftime('%Y', begindatum) AS jaar, strftime('%m', begindatum) AS maand, maandnaam, count(*) AS count_1 "
    "FROM(SELECT begindatum, maandnaam"
    "     FROM Straatroven)"
    "GROUP BY jaar, maand",
               'sqlite:///data/Opendata.db')

list_dict =[]
for i in plot1sql:
    print(i)
    dict = {'date': i.maandnaam + "-" + i.jaar, 'value': i.count_1 }
    list_dict.append(dict)

return list_dict
