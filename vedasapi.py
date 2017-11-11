import requests
import json
from datetime import datetime, timedelta

latitude = [22.797222, 21.499166, 23.801111]
longitude = [72.57083, 70.44334, 69.50166]

'''
6apr 2012
6sep 2017
'''

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
