#!/usr/bin/env python
# coding: utf-8

# In[20]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[21]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[23]:


# First, I downloaded four diferent databases; 
# 'Poverty' includes a list of every country classified by region and 4 diffetent types of income groups, among other data.
# 'Religions' includes the religious composition per country, among other data.
# 'PIB' includes a list of every country and its GDP, among other data.
# 'Weather' includes the yearly weather average per country, among other data.
# After the downloading was finished, I began cleaning the data.

Poverty = "Path"
Religions = "Path"
PIB = "Path"
Weather = "Path"


Poverty_df = pd.read_csv(Poverty)
Religions_df = pd.read_csv(Religions)
PIB_df = pd.read_csv(PIB)
Weather_df = pd.read_csv(Weather)


# In[24]:


# Filtering information by Income Group

Poverty_df = Poverty_df[["TableName","Region","IncomeGroup"]]
Poverty_df = Poverty_df.dropna()

Poverty_high_df = Poverty_df.loc[Poverty_df["IncomeGroup"]=="High income"]
Poverty_low_df = Poverty_df.loc[Poverty_df["IncomeGroup"]=="Low income"]
Poverty_lower_df = Poverty_df.loc[Poverty_df["IncomeGroup"]=="Lower middle income"]
Poverty_upper_df = Poverty_df.loc[Poverty_df["IncomeGroup"]=="Upper middle income"]


# In[25]:


# Country - Temperature (ºC) correlation
Weather_df = Weather_df[["Country","Annual_temp"]]
Weather_df.head()


# In[26]:


# Filtering Country information by Region
Poverty_df = Poverty_df.rename(columns={"TableName":"Country"})
Poverty_df.head()


# In[27]:


# Selecting religion values for 2020 year

Religions_df = Religions_df[["Country","Year",
                             "Christians","Muslims",
                             "Hindus","Buddhists","Folk Religions",
                             "Jews","Other Religions","Unaffiliated"]]

reli_df = Religions_df.loc[(Religions_df["Year"] == 2020)]


reli_df.head()


# In[28]:


# Dropping NaN rows and selecting the 2018 year, since it was the most recent
PIB_df = PIB_df.dropna()
PIB_df = PIB_df[["Country","2018"]]

PIB_df.head()


# In[29]:


# Merge #1: merging the income and region dataframe with the GDP dataframe
Merge1_df = pd.merge(Poverty_df, PIB_df, how='outer', on='Country')

Merge1_df.head()


# In[30]:


# Merge #2: taking the first merge and adding the religion dataframe
merge2_df = pd.merge(Merge1_df, reli_df, how='outer', on='Country')
merge2_df.head()


# In[31]:


# Merge #3: taking the second merge and adding the weather dataframe
merge3_df = pd.merge(merge2_df, Weather_df, how='outer', on='Country')
merge3_df


# In[32]:


# Final merge: dropping nan rows and the 'Year' column and renaming certain columns.
super_merge_df = merge3_df.dropna()
super_merge_df = super_merge_df.drop(["Year"],axis=1)
super_merge_df = super_merge_df.rename(columns={"2018":"PIB",
                                                "Unaffiliated":"Unaffiliated Religions",
                                                "Annual_temp":"Annual Temperature"})
super_merge_df


# In[190]:


# Saving the new dataframe into a new CSV file
super_merge_df.to_csv("Final_DF.csv",
                  encoding="utf-8", index=False, header=True)

