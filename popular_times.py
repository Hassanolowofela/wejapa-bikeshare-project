#Compute the Most Popular Start Hour
#Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling. There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time" column. To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime()

#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html

  #method and extracting properties such as the hour with these properties. - https://pandas.pydata.org/pandas-docs/stable/api.html#datetimelike-properties

#Hint: Another way to describe the most common value in a column is the mode.

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = 

# convert the Start Time column to datetime
df['Start Time'] =

# extract hour from the Start Time column to create an hour column
df['hour'] =

# find the most common hour (from 0 to 23)
popular_hour = 
    
print('Most Frequent Start Hour:', popular_hour)
