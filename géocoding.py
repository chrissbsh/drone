#setup
import urllib.request
import json
from math import *


from opencage.geocoder import OpenCageGeocode

key = '7ec07c47db6749d9a436cde14a5aface'
geocoder = OpenCageGeocode(key)


#entré de l'adresse

L=input("autoriser la localisation , oui ou non ? :")

if "OUI"in L.upper():
    l2=48.684179
    ln2=2.353044
    print(l2,",",ln2)

else:
    rue = input("adresse : ")
    codepostal = input("code postal : ")
    ville = input("ville : ")

    R0=rue.replace("â", "a").replace("È", "e").replace("É", "e").replace("è", "e").replace("é", "e").replace("'", "%27").replace(" ", "%20")

    V0=ville.replace("â", "a").replace("È", "e").replace("É", "e").replace("è", "e").replace("é", "e").replace("'", "%27").replace(" ", "%20")



    R1=R0.upper()
    CP1=codepostal.upper()
    V1=V0.upper()

    #R3=R2+","
    #CP2=CP1+","

    Q=(R1+ " "+ V1)
    print(Q)

    Q1=(R1+"%20"+CP1+"%20"+V1)

    print(Q1)

    url1=("https://api.opencagedata.com/geocode/v1/json?q="+Q1+",%20FRANCE&key=7ec07c47db6749d9a436cde14a5aface&language=fr&pretty=1")

    print(url1)

    #geocoding
    #url = "https://api.opencagedata.com/geocode/v1/json?q=PARIS,%20FRANCE&key=7ec07c47db6749d9a436cde14a5aface"

    q = urllib.request.urlopen(url1)

    data = json.load(q)

    #print(data)


    #query = u', , 21 PLACE DE JOFFRE PARIS, France'

    query2=("u', , " + Q + " " + 'France')

    print(query2)

    results = geocoder.geocode(query2)

    print(u'%f;%f' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],))
                        #results[0]['components']['country_code'],
                        #results[0]['annotations']['timezone']['name']))



    lat = results[0]['geometry']['lat']

    lng = results[0]['geometry']['lng']

    l2 = float(lat)
    ln2 = float(lng)


l1=float(48.6333)
ln1=float(2.45)


A=fabs(l1-l2)
print("A:" , A)

B=fabs(ln1-ln2)
print("B:" , B)

#angle
alpha=float(tan(B/A))
print(alpha,"rad")

ALPHA=degrees(alpha)
print(ALPHA ,"°")

#distance
T=int(6371000)
phi1=l1*pi/180
phi2=l2*pi/180
Dphi1=A*pi/180
Dphi2=B*pi/180

k=sin(Dphi1/2)*sin(Dphi1/2)+cos(phi1)*cos(phi2)*sin(Dphi2/2)*sin(Dphi2/2)

j=2*atan2(sqrt(k),sqrt(1-k))

d=T*j

print("distance: ", d , "m")