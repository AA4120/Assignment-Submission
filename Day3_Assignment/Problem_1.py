#Explore the given data set
import pandas as pd
import numpy as np
df=pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')
print(df.head())
print(df["item_name"])
print(df.loc[2])
print(df.iloc[:,1:])
print(df.isnull().sum())
print(df.describe())
print(df.shape)
print(df.info())
print(df.corr())
print(df.dropna(axis=0))
print(df.dtypes)
print(df['sort_sequence'][1])
print(df['sort_sequence'].value_counts())
print(df[df['sort_sequence']<5])
