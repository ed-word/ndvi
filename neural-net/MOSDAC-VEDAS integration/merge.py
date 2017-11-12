import pandas as pd

df1 = pd.read_csv('api.csv')
df2 = pd.read_csv('edit.csv')

df = pd.merge(left=df1,right=df2,how='inner',on=['LATITUDE','LONGITUDE','DATE(IST)'])
df.to_csv('merge.csv', index=False)