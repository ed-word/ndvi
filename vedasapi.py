import requests
import json

latitude = [22.797222, 21.499166, 23.801111]
longitude = [72.57083, 70.44334, 69.50166]

'''
6apr 2012
6sep 2017
'''

for (la, lg) in zip(latitude, longitude):
	la = "latitude=" + str(la)
	lg = "&longitude=" + str(lg)
	params = la + lg

	url = "http://vedas.sac.gov.in:8080/LeanGeo/api/band_val/NDVI_OCM?" + params
	response = requests.request("GET", url)
	json_data = json.loads(response.text)
