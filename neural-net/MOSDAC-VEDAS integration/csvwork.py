import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('data.csv', low_memory=False)

df = df.dropna()

df = df[[
	'LATITUDE', 'LONGITUDE', 'DATE(IST)',
	'AIR_TEMPERATURE',
	'SOIL_TEMPERATURE',
	'SOIL_MOISTURE',
	'RAINFALL'
]]


def dates(row):
	val = str(row['DATE(IST)'])
	val = datetime.strptime(val, "%d/%m/%Y")
	val = datetime.strftime(val, "%d/%m/%Y").replace('/0', '/')
	if val[0] == '0':
		val = val[1:]
	return val


df = df.drop_duplicates(subset=['LATITUDE', 'LONGITUDE','DATE(IST)'])
df['DATE(IST)'] = df['DATE(IST)'].replace(to_replace='-', value='/', regex=True)
df['DATE(IST)'] = df.apply(dates, axis=1)     		

df.to_csv('edit.csv', index=False)
