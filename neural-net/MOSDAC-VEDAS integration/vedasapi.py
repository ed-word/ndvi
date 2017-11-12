import requests
import json
from datetime import datetime, timedelta
import pandas as pd

'''
df = pd.read_csv('edit.csv')
lat = df['LATITUDE']
lon = df['LONGITUDE']

x = lat[0]
lalist = [lat[0]]
lolist = [lon[0]]
for la,lo in zip(lat, lon):
	if la != x:
		x = la
		lalist.append(la)
		lolist.append(lo)


print(lalist)
print(lolist)
'''

latitude = [16.779, 17.340279000000002, 22.797222000000001, 21.499165999999999, 8.298055999999999, 13.621111000000001, 30.592222, 22.696667000000001, 30.334444000000001, 22.363056, 23.915555999999999, 27.199999999999999, 23.058890000000002, 25.979165999999999, 19.717222]
longitude = [75.75, 78.592224000000002, 72.570830000000001, 70.443340000000006, 77.55583, 80.226943999999975, 76.262500000000003, 77.744445999999996, 78.000275000000002, 80.58278, 81.103059999999999, 77.450000000000003, 88.544440000000023, 85.666390000000007, 85.194725000000005]

'''
6apr 2012
6sep 2017
'''

with open("api.csv", "w") as f:
	f.write("LATITUDE,LONGITUDE,VALUE,DATE(IST)\n")

for (lati, longi) in zip(latitude, longitude):
	la = "latitude=" + str(lati)
	lg = "&longitude=" + str(longi)
	params = la + lg

	url = "http://vedas.sac.gov.in:8080/LeanGeo/api/band_val/NDVI_OCM?" + params
	response = requests.request("GET", url)
	json_data = json.loads(response.text)
	with open("api.csv", "a") as f:
		init_time = 1333737000000
		s = '06/04/2012'
		dt = datetime.strptime(s, "%d/%m/%Y")
		for j in json_data:
			row = ''
			row += str(lati)
			row += ","
			row += str(longi)
			row += ","
			row += str(j['value'])
			row += ","
			mseconds = j['time']-init_time
			dt = dt + timedelta(milliseconds=mseconds)
			strdate = datetime.strftime(dt, "%d/%m/%Y").replace('/0', '/')
			if strdate[0] == '0':
				strdate = strdate[1:]
			row += strdate + '\n'
			init_time = j['time']
			f.write(row)
