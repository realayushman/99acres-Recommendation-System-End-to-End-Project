# -*- coding: utf-8 -*-
"""Kolkata Data cleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CmhnSIVAF37xAo3ycXfa38Sf1SPkYTZz
"""

import pandas as pd

df=pd.read_csv("kolkata.csv")

df

df.columns

df['city']=df['CITY'].str.lower()

df.city.value_counts()

df["side"]=df['city'].str.split().str[-1]

df.side.value_counts()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['side']=le.fit_transform(df.side)

df.side

df.columns

df['FEATURES']

df['BALCONY_NUM'].fillna(0,inplace=True)

import ast
df['lat_long']=df['MAP_DETAILS'].apply(ast.literal_eval)
df['latitude']=df['lat_long'].apply(lambda x:x['LATITUDE'])
df['longitude']=df['lat_long'].apply(lambda x:x['LONGITUDE'])

df['FEATURES']=df['FEATURES'].replace('N',0)

df['society']=df['SOCIETY_NAME'].str.lower()

df=df[df.PRICE!="Price on Request"]

df



df['latitude']

df[['MAP_DETAILS']]

df["preference"]=le.fit_transform(df.PREFERENCE)

df.preference.value_counts()

df.PROPERTY_TYPE.value_counts()

df['TRANSACT_TYPE'].value_counts()

df['TRANSACT_TYPE'].fillna(0,inplace=True)

df['OWNTYPE']

df['type']=le.fit_transform(df["PROPERTY_TYPE"])

df.columns

df.AMENITIES.fillna(0,inplace=True)

df[['FEATURES','PREFERENCE']]













#possible drop cols
'PROP_ID','PROP_NAME','SOCIETY_NAME','location','BUILDING_NAME','FORMATTED_LANDMARK_DETAILS','SECONDARY_TAGS','PROP_HEADING','MAP_DETAILS','CITY','PROPERTY_TYPE','DESCRIPTION','SUPERBUILTUP_SQFT'

#count go deep
'location','FORMATTED_LANDMARK_DETAILS'

#might use nlp
'BUILDING_NAME','SECONDARY_TAGS','PROP_HEADING','DESCRIPTION'

df

df.isnull().sum()

df[['AREA','BUILTUP_SQFT','SUPER_AREA','SUPERBUILTUP_SQFT','CARPET_SQFT']]

'BEDROOM_NUM','FLOOR_NUM','CARPET_SQFT'

df.to_csv('clean_kolkata.csv', index=False)

from google.colab import files
files.download('clean_kolkata.csv')

