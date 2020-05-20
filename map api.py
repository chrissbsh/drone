import urllib.request
import json
from math import *

import googlemaps

gmaps = googlemaps.Client(key='KEY')

L=input("autoriser la localisation , oui ou non ? :")

if "OUI"in L.upper():
    url1 = ("http://api.ipstack.com/check?access_key='key")
    q = urllib.request.urlopen(url1)
    data = json.load(q)
    # print(data)

    ip = data['ip']
    # print(ip)

    url = ("http://api.ipstack.com/" + ip + "?access_key='key")

    q = urllib.request.urlopen(url)
    data = json.load(q)
    print(data)

    l2 = (data['latitude'])
    ln2 = (data['longitude'])

    print(l2)
    print(ln2)

else:

    rue = input("adresse : ")
    codepostal = input("code postal : ")
    ville = input("ville : ")

    R0=rue.replace("â", "a").replace("È", "e").replace("É", "e").replace("è", "e").replace("é", "e").replace(" ", "+").replace("'", "%27")

    V0=ville.replace("â", "a").replace("È", "e").replace("É", "e").replace("è", "e").replace("é", "e").replace(" ", "+").replace("'", "%27")

    R1=R0.upper()
    CP1=codepostal.upper()
    V1=V0.upper()

    Q1=(R1+"%2C"+CP1+"+"+V1+"%2C")
    print(Q1)

    url =("https://maps.googleapis.com/maps/api/geocode/json?address="+Q1+"+FRANCE&autocomplete=1&key='key")

    print(url)

    #geocoding
    q = urllib.request.urlopen(url)

    data = json.load(q)
    #print(data)

    geocode_result = gmaps.geocode(Q1)
    #print(geocode_result)

    print(geocode_result[0]['geometry']['location']['lat'])
    print(geocode_result[0]['geometry']['location']['lng'])

    lat=geocode_result[0]['geometry']['location']['lat']
    lng=geocode_result[0]['geometry']['location']['lng']

    l2 = float(lat)
    ln2 = float(lng)

l1=float(48.637976)
ln1=float(2.443590)

A=fabs(l1-l2)
#print("A:" , A)

B=fabs(ln1-ln2)
#print("B:" , B)

#angle
alpha=float(tan(B/A))
print(alpha,"rad")

ALPHA=degrees(alpha)
print(ALPHA ,"°")

#distance
T=int(6371009)
phi1=l1*pi/180
phi2=l2*pi/180
Dphi1=A*pi/180
Dphi2=B*pi/180

k=sin(Dphi1/2)*sin(Dphi1/2)+cos(phi1)*cos(phi2)*sin(Dphi2/2)*sin(Dphi2/2)

j=2*atan2(sqrt(k),sqrt(1-k))

d=T*j

print("distance: ", d, "m")
