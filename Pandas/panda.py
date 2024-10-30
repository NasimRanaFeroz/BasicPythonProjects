import pandas as pd

#df = pd.read_csv("weather.csv")
#print(df['Avg Temp'].max())
#print(df['Avg Temp'].mean())
#print(df['Avg Temp'].describe())

df = pd.read_csv("weather.csv")
print(df[df['Avg Temp']==df['Avg Temp'].max()])