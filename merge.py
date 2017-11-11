import pandas as pd

df1 = pd.read_csv('api.csv')
df2 = pd.read_csv('edit.csv')

df = df1[['LATITUDE','LONGITUDE','DATE(IST)']]
df2 = df2[['LATITUDE','LONGITUDE','DATE(IST)']]
df = pd.merge(left=df,right=df2,on=['LATITUDE','LONGITUDE','DATE(IST)'])
df.to_csv('merge.csv', index=False)