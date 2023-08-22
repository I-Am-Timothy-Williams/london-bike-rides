# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:59:31 2023

@author: Timot
"""

import pandas as pd
# import ZipFile
# import kaggle


#!kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset
#extract files from zip file
zipfile_name = 'london-bike-sharing-dataset.zip'

# with zipfile.ZipFile(zipfile_name, 'r' == file):
#     file.extractall()
    
#read in csv files as pd dataframe

bikes = pd.read_csv("london_merged.csv")

#explore the data
print(bikes.info())
print(bikes.shape)
print(bikes)

#count unique values in the weather_code column
print(bikes.weather_code.value_counts())
print(bikes.season.value_counts())

#defining column names that I want to use
new_cols_dict = {
        'timestamp': 'time',
        'cnt': 'count',
        't1':'temp_real_C',
        't2':'temp_feels_like_C',
        'hum':'humidity_percent',
        'wind speed':'wind_speed_kph',
        'weather_code':'weather',
        'is_holiday':'is_holiday',
        'is_weekend':'is_weekend',
        'season':'season'
        }

#renaming columns to specified column names
bikes.rename(new_cols_dict,axis=1,inplace=True)

#normalizing humidty values to values between 0 and 1
bikes.humidity_percent = bikes.humidity_percent/100

#Mapping integers between 0-3 to actual season names
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'fall',
    '3.0':'winter'
    }

#Mapping integers to Weather Descriptions
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered Clouds',
    '3.0':'Broken Clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with Thunderstorm',
    '26.0':'Snowfall'
    }

#changing the seasons column data type to string and mapping values to names
bikes.season = bikes.season.astype('str')
bikes.season = bikes.season.map(season_dict)


#changing the weather column data type to string and mapping values to names
bikes.weather = bikes.weather.astype('str')
bikes.weather = bikes.weather.map(weather_dict)

#check df to see if it worked

bikes.head()
bikes.to_excel('london_bikes_final2.xlsx', sheet_name = 'Data')