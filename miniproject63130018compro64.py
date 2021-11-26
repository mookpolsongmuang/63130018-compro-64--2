print("Aircraft conflict counter")
print("This program count incident(s) when following condition are met")
print("1.Aircraft gets closer than 3 nautical miles")
print("2.Aircraft altitude is less than 1000 feet")
import pandas as pd
from math import cos, sin, asin, sqrt, radians

def baroaltcheck(baroaltitude1,baroaltitude2):
    b = abs(baroaltitude2-baroaltitude1)
    return b
def distancecheck(lat1,lat2,lon1,lon2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    dlat = abs(lat2-lat1)
    dlon = abs(lon2-lon1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    d = abs(2 * asin(sqrt(a))*3440)
    return d
y = 0
z = 0
df = pd.read_csv(r'D:\nightmare\year 2\programming\63130018 compro 64\day4.csv')
df = df [df.onground==False]
df = df.drop(columns=["velocity","icao24","heading","vertrate","alert","spi","squawk","onground","geoaltitude","lastposupdate","lastcontact","hour"])
df = df.sort_values(["time"])
df = df.reset_index(drop=True)
#print(df)
for i in df.index:
    j = i+1
    if j not in df.index:
        break
    while df.at[i, "time"] == df.at[j, "time"] :
        if baroaltcheck(df.at[i, "baroaltitude"], df.at[j, "baroaltitude"]) <= 304.8:
            z +=1
        if distancecheck(df.at[i,'lat'], df.at[j,'lat'], df.at[i,"lon"], df.at[j,'lon']) <=3:
            y +=1
        print(i, j)
        j +=1
        if j not in df.index:
            break
q = y+z
print("there is a ",z,"vertical incident(s).")
print("there is a ",y,"horizontal incident(s).")
print("there is a total of",q,"total incident(s).")
if q >= 1:
    print("SOMEONE IS IN TROUBLE FROM THEIR BOSS!!!")