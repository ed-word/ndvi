import pandas as pd

df = pd.read_csv('data.csv', low_memory=False)

df = df.dropna()

df = df[[
	'LATITUDE', 'LONGITUDE', 'DATE(IST)',
	'AIR_TEMPERATURE',
	'SOIL_TEMPERATURE',
	'SOIL_MOISTURE',
	'RAINFALL'
]]

df = df.drop_duplicates(subset='DATE(IST)')
df['DATE(IST)'] = df['DATE(IST)'].replace(to_replace='-', value='/', regex=True)
df['DATE(IST)'] = df['DATE(IST)'].replace(to_replace='/0', value='/', regex=True)

df.to_csv('edit.csv', index=False)
