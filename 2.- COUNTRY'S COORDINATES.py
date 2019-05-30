#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

import gmaps

# Google developer API key
gkey = "GKEY"

# Access maps with unique API key
gmaps.configure(gkey)

# Import API key
import json
import requests
api_key = "API KEY"

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"


# In[14]:


#Loading the final merge from the cleaning notebook and creating a dataframe from it
raw = 'Path/Final_DF.csv'
df = pd.read_csv(raw)
df.head()


# In[15]:


#Creating a list from the 'Country' column in the dataframe
list1 = list(df['Country'])


# In[16]:


#Creating three empty lists, which eventually will store each country's latitude and longitude
city1 = []
latitude = []
longitude = []
#Creating a 'for' loop that will make calls to the google maps' API por each element in the 'Country' list previously created.
for city in list1:
    target_url = ('https://maps.googleapis.com/maps/api/geocode/json?'
    'address={0}&key={1}').format(city, gkey)
    geo_data = requests.get(target_url).json()
    res=geo_data['results']
    first=res[0]
#Obtain the geometry and location.    
    geo = first['geometry']['location']
#Obtain the latitude and longitude from each result.        
    lat=geo['lat']
    lng=geo['lng']
#Append each latitude and longiude coordInates to the previously created lists, as well as each country.
    longitude.append(lng)
    latitude.append(lat)
    city1.append(city)


# In[17]:


#Create two new dataframes from the latitude and longitude lists  
df1 = pd.DataFrame(latitude)
df2 = pd.DataFrame(longitude)


# In[18]:


#Merge both dataframes
df_merge = df2.merge(df1, how='outer', left_index=True, right_index=True)

#Create a new dataframe with the columns from the last merge renamed.
new_data = df_merge.rename(columns = {"0_y": "Longitude", 
                                  "0_x": "Latitude" }) 
#Change the new dataframe's index.
new_data.index = city1
new_data.index.name = 'Country'

new_data


# In[ ]:


# Saving the new dataframe into a new CSV file
new_data_df.to_csv("cities.csv", encoding="utf-8", index=False, header=True)

