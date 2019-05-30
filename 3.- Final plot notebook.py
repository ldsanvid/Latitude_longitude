#!/usr/bin/env python
# coding: utf-8

# In[70]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[71]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[72]:


# Reading the csv that is a merge of the dataframe that includes religion, annual temperature, gdp, region, income group per country
# with the latitude and longitude dataframe

file = "Path/Merge_Final1numero.csv"

Latitude_df = pd.read_csv(file)
Latitude_df.head()


# In[73]:


# Selecting specific columns

Whole_df = Latitude_df[["Country","Annual Temperature","Longitude","Latitude","PIB","IncomeGroup"]]

Whole_df.head(10)


# In[74]:


# Sorting "PIB"(GDP) column values 

pib_desc_df = Whole_df.sort_values(["PIB"], ascending=False)

pib_desc_df.head(10)


# In[75]:


# Finding values for Mexico row

mex = Whole_df.loc[Whole_df["Country"]=="Mexico"]
mex


# In[76]:


# Finding row values for the highest GDP Country values below the Equator

south_maxpib_df = Whole_df.loc[(Whole_df["Latitude"] < 0)]
south_maxpib_df = south_maxpib_df.sort_values(["PIB"], ascending=False)
south_maxpib_df = south_maxpib_df.iloc[[0]]
south_maxpib_df


# In[77]:


# PLOTTING

lati = list(Whole_df["Latitude"])
pibi = list(Whole_df["PIB"])

Size = [x/100 for x in pibi]


# Plotting all values
lat_pib = plt.scatter(lati, pibi, marker="o", facecolors="gainsboro", edgecolors="black", s=Size)


# Plotting specific values
qatar =      plt.scatter( pib_desc_df.iloc[0,3], pib_desc_df.iloc[0,4], 
                          marker="o", facecolors="yellow", edgecolors="black", 
                          s=pib_desc_df.iloc[0,4]/100, label="Qatar")
luxembourg = plt.scatter( pib_desc_df.iloc[1,3], pib_desc_df.iloc[1,4], 
                          marker="o", facecolors="darkviolet", edgecolors="black", 
                          s=pib_desc_df.iloc[1,4]/100, label="Luxembourg")
ireland =    plt.scatter( pib_desc_df.iloc[2,3], pib_desc_df.iloc[2,4], 
                          marker="o", facecolors="coral", edgecolors="black", 
                          s=pib_desc_df.iloc[2,4]/100, label="Ireland")
usa =        plt.scatter( pib_desc_df.iloc[7,3], pib_desc_df.iloc[7,4], 
                          marker="o", facecolors="dodgerblue", edgecolors="black", 
                          s=pib_desc_df.iloc[7,4]/100, label="USA")
mexico =     plt.scatter( Whole_df.iloc[83,3], Whole_df.iloc[83,4], 
                          marker="o", facecolors="limegreen", edgecolors="black", 
                          s=Whole_df.iloc[83,4]/100, label="Mexico")
australia =  plt.scatter( Whole_df.iloc[6,3], Whole_df.iloc[6,4], 
                          marker="o", facecolors="red", edgecolors="black", 
                          s=Whole_df.iloc[6,4]/100, label="Australia")

# Lines
plt.grid(True)

#Ecuador
plt.vlines(0, -5000, 1000000, alpha=1, color="r", linestyles="dashed")

#Tropic of Cancer
plt.vlines(23, -5000, 1000000, alpha=1, color="b", linestyles="dashed")

#Tropic of Capricorn
plt.vlines(-23, -5000, 1000000, alpha=1, color="g", linestyles="dashed")

plt.ylim(-5000,145000)


# Legend
plt.legend(handles=[qatar, luxembourg, ireland, usa, mexico, australia], markerscale=0.38, loc="best")

# Axis names
plt.title("Countries PIB by Latitude")
plt.xlabel("Latitude (Degrees)")
plt.ylabel("Per Capita PIB (Units)")

# Saving PNG
plt.savefig("Path/lat_pib_coun.png")


plt.show(lat_pib)


# In[ ]:


#Conclusion of this plot: The further a country is from the Ecuador, the bigger its GDP is.


# In[78]:


# DataFrames by Income Group

country_income_low= Whole_df.loc[Whole_df["IncomeGroup"]=="Low income"]
country_income_lomi= Whole_df.loc[Whole_df["IncomeGroup"]=="Lower middle income"]
country_income_upmi= Whole_df.loc[Whole_df["IncomeGroup"]=="Upper middle income"]
country_income_high= Whole_df.loc[Whole_df["IncomeGroup"]=="High income"]


# In[79]:


# Example of High Income Countries

country_income_high.head()


# In[80]:


# Also included a transparency column from the Transparency Index per country. 
# Here, I'm uploading a csv file with a merge of the general dataframe with the transparency index column 

file2 = "Path/Merge_Final1 (1).csv"

Whole_df_2 = pd.read_csv(file2)
Whole_df_2


# In[81]:


# PLOTTING LONGITUDE vs LATITUDE

#Creating lists per income group
longi_high = list(country_income_high["Longitude"])
lati_high = list(country_income_high["Latitude"])

longi_low = list(country_income_low["Longitude"])
lati_low = list(country_income_low["Latitude"])

longi_high_mi = list(country_income_upmi["Longitude"])
lati_high_mi = list(country_income_upmi["Latitude"])

longi_low_mi = list(country_income_lomi["Longitude"])
lati_low_mi = list(country_income_lomi["Latitude"])


#Plotting per income group:

lat_lng_income_high =    plt.scatter(longi_high, lati_high, marker="o", 
                                     facecolors="red", edgecolors="black",
                                     s=500, label="High Income")
lat_lng_income_high_mi = plt.scatter(longi_high_mi, lati_high_mi, marker="o", 
                                     facecolors="yellow", edgecolors="black", 
                                     s=300, label="Upper Middle Income")
lat_lng_income_low_mi =  plt.scatter(longi_low_mi, lati_low_mi, marker="o", 
                                     facecolors="green", edgecolors="black", 
                                     s=150, label="Lower Middle Income")
lat_lng_income_low =     plt.scatter(longi_low, lati_low, marker="o",
                                     facecolors="b", edgecolors="black", 
                                     s=50, label="Low Income")

#Saving in a variable the Ecuador and plotting it
Ecuador = plt.hlines(0, -180, 200, alpha=1, color="darkslategray", linestyles="dashed")

plt.grid(True)





plt.xlim(-150,200)
plt.ylim(-90,90)

# Legend
plt.legend(handles=[lat_lng_income_high, lat_lng_income_high_mi, 
                    lat_lng_income_low_mi, lat_lng_income_low], 
                    markerscale=0.7, loc=8)

# Axis names
plt.title("Countries by Income Group in the World")
plt.xlabel("Longitude (Degrees)")
plt.ylabel("Latitude (Degrees)")

# Saving png
plt.savefig("Path/lon_lat_IncomeGroup.png")


# In[ ]:


#Conclusion of this plot: The further a country is from the Ecuador, the higher its income level is.


# In[82]:


# Sorting countries by Transparency

top_trans_df = Whole_df_2.sort_values(["Transparency "], ascending=False)
top_trans_df = top_trans_df[["Country","Transparency ","PIB"]]
top_trans_df = top_trans_df.reset_index()
top_trans_df = top_trans_df[["Country","Transparency ","PIB"]]
top_trans_df.head(10)


# In[83]:


# Finding values for the USA row

usa_2 = top_trans_df.loc[top_trans_df["Country"]=="UNITED STATES"]
usa_2


# In[84]:


# Finding values for the Mexico row

mex_2 = top_trans_df.loc[top_trans_df["Country"]=="MEXICO"]
mex_2


# In[85]:


# PLOT : TRANSPARENCY vs GDP

trans = list(Whole_df_2["Transparency "])
pibis = list(Whole_df_2["PIB"])

Sizes = [x/100 for x in pibis]


# Plotting all values
trans_pib = plt.scatter(trans, pibis, marker="o", facecolors="lightcyan", edgecolors="black", s=Sizes)


# Plotting specific values
denmark_2 =      plt.scatter( top_trans_df.iloc[0,1], top_trans_df.iloc[0,2], 
                          marker="o", facecolors="yellow", edgecolors="black", 
                          s=top_trans_df.iloc[0,2]/100, label="Denmark")

new_zealand_2 = plt.scatter( top_trans_df.iloc[1,1], top_trans_df.iloc[1,2], 
                          marker="o", facecolors="orange", edgecolors="black", 
                          s=top_trans_df.iloc[1,2]/100, label="New Zealand")

luxembourg_2 = plt.scatter( top_trans_df.iloc[8,1], top_trans_df.iloc[8,2], 
                          marker="o", facecolors="darkviolet", edgecolors="black", 
                          s=top_trans_df.iloc[8,2]/100, label="Luxembourg")

usa_2 =        plt.scatter( top_trans_df.iloc[20,1], top_trans_df.iloc[20,2], 
                          marker="o", facecolors="dodgerblue", edgecolors="black", 
                          s=top_trans_df.iloc[20,2]/100, label="USA")

mexico_2 =     plt.scatter( top_trans_df.iloc[108,1], top_trans_df.iloc[108,2], 
                          marker="o", facecolors="limegreen", edgecolors="black", 
                          s=top_trans_df.iloc[108,2]/100, label="Mexico")

south_sudan_2 =  plt.scatter( top_trans_df.iloc[138,1], top_trans_df.iloc[138,2], 
                          marker="o", facecolors="red", edgecolors="red", 
                          s=top_trans_df.iloc[138,2]/100, label="South Sudan")



# Legend
plt.legend(handles=[denmark_2, new_zealand_2, 
                    luxembourg_2, usa_2, mexico_2, south_sudan_2], 
                    markerscale=0.475, loc="best")

plt.grid(True)


plt.ylim(-3500,145000)

# Axis names
plt.title("Countries PIB by Transparency in the World")
plt.xlabel("Transparency Index (Units)")
plt.ylabel("Per Capita PIB (Units)")

# Saving png
plt.savefig("Path/trans_pib_coun.png")


# In[ ]:


#Conclusion of this plot: Countries with the biggest GDPs have the highest scores in the transparency index.


# In[86]:


# Sorting by Trasnparecny again but in terms of Temperature

trans_tem_df = Whole_df_2.sort_values(["Transparency "], ascending=False)
trans_tem_df = trans_tem_df[["Country","Annual Temperature","Transparency "]]
trans_tem_df = trans_tem_df.reset_index()
trans_tem_df = trans_tem_df[["Country","Annual Temperature","Transparency "]]

trans_tem_df.head()


# In[87]:


# Showing the coldest country transparency values

trans_tem_desc_temp_df = trans_tem_df.sort_values(["Annual Temperature"], ascending=False)
trans_tem_desc_temp_df = trans_tem_desc_temp_df.reset_index()
trans_tem_desc_temp_df = trans_tem_desc_temp_df[["Country","Annual Temperature","Transparency "]]
trans_tem_desc_temp_df.tail()


# In[88]:


# PLOT : TEMPERATURE vs TRANSPARENCY

trans = list(trans_tem_df["Transparency "])
temps = list(trans_tem_df["Annual Temperature"])

Sizes2 = [x*3 for x in trans]


# Plotting all values
trem_trans = plt.scatter(temps, trans, marker="o", facecolors="lightcyan", edgecolors="black", s=Sizes2)


# Plotting specific values

denmark_3 =     plt.scatter( trans_tem_df.iloc[0,1], trans_tem_df.iloc[0,2], 
                          marker="o", facecolors="yellow", edgecolors="black", 
                          s=trans_tem_df.iloc[0,2]*3, label="Denmark")

new_zealand_3 = plt.scatter( trans_tem_df.iloc[1,1], trans_tem_df.iloc[1,2], 
                          marker="o", facecolors="orange", edgecolors="black", 
                          s=trans_tem_df.iloc[1,2]*3, label="New Zealand")

canada_3 =   plt.scatter( trans_tem_desc_temp_df.iloc[138,1], trans_tem_desc_temp_df.iloc[138,2], 
                          marker="o", facecolors="darkviolet", edgecolors="black", 
                          s=trans_tem_desc_temp_df.iloc[138,2]*3, label="Canada")

usa_3 =        plt.scatter( trans_tem_df.iloc[20,1], trans_tem_df.iloc[20,2], 
                          marker="o", facecolors="dodgerblue", edgecolors="black", 
                          s=trans_tem_df.iloc[20,2]*3, label="USA")

mexico_3 =     plt.scatter( trans_tem_df.iloc[108,1], trans_tem_df.iloc[108,2], 
                          marker="o", facecolors="limegreen", edgecolors="black",
                          s=trans_tem_df.iloc[108,2]*3, label="Mexico")



# Axis names
plt.title("Countries Transparency by Temperature")
plt.xlabel("Annual Temperature (ºC)")
plt.ylabel("Transparency Index (Units)")

#Reference lines (in blue)
plt.vlines(0, 0, 100, alpha=1, color="blue", linestyles="dashed")

plt.vlines(12, 0, 100, alpha=1, color="blue", linestyles="dashed")

plt.hlines(80, -20, 32, alpha=1, color="blue", linestyles="dashed")



plt.ylim(0,100)
plt.xlim(-12,30)

plt.grid(True)

# Legend
plt.legend(handles=[denmark_3, new_zealand_3, 
                    usa_3, mexico_3, canada_3], 
                    markerscale=0.475, loc="best")



# Saving png
plt.savefig("Path/temp_trans.png")


# In[ ]:


#Conclusion of this plot: Countries with the biggest GDPs have both an annual temperature
#between 0° and 12° C and a near or above eighty score in the transparency index.

