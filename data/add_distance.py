from geopy.distance import vincenty
from query import *

policeq = query("SELECT naam, latitude, longitude FROM police_stations")
roofq = query("SELECT voorval_nr, latitude, longitude FROM Straatroven")

i = 0
for r in roofq:
    i = i + 1
    print(r)
print(i)

if __name__ == '__main__':
    pass