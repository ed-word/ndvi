import pandas as pd

df = pd.read_csv('data.csv', low_memory=False)

df = df[pd.notnull(df)]

df = df[[
	'LATITUDE', 'LONGITUDE', 'DATE(IST)',
	'AIR_TEMPERATURE1(°C at 2m height)',
	'SOIL_TEMPERATURE1(°C at 0.50m height)',
	'SOIL_MOISTURE',
	'RAINFALL(mm)'
]]


start_date = "06/04/2012"
end_date = "06/09/2017"

'''
def dates(row):
	val = row['DATE(IST)']

	if val == 0:
		count += 1
		if count > 500:
			return float('NaN')
	return val
'''

df.drop_duplicates(subset='DATE(IST)')
#df['DATE(IST)'] = df.apply(dates, axis=1)
#df = df[pd.notnull(df['DATE(IST)'])]

df.to_csv('edit.csv', index=False)
