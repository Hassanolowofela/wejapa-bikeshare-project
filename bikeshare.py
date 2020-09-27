import pandas as pd
import datetime as dt
import calendar
import numpy as np
from time import time

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }
print("A Wonderful day to you great Mentor!")


def load_data(city, month, day):
    while True:
        try:
            # load data file into a dataframe
            City = str(input(" Would you like to see data for Chicago, New York, or Washington? \n")).strip()
            df = pd.DataFrame(pd.read_csv(CITY_DATA[City]))
        except (KeyError, NameError, TypeError, ValueError):
            print(" Oooops!\n Please use the appropriate name and begin with a capital letter (e.g. city: Chicago) ")
        else:
            break
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y/%m/%d %H:%M:%S')

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month_name()
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).day_name()

    filter_words = ['month', 'day', 'both']

    while True:
        try:
            filter_option = str(input(" How would you like your data filtered?\n please enter any of the options given below:\n month\n day\n both \n"))

            if filter_option == 'month':
                while True:
                    try:
                        month1 = str(input(" Please choose a month between January and June. Ensure to begin with a 'Capital letter'.(e.g. January)\n"))
                        if month1 != 'both':
                            # use the index of the months list to get the corresponding int
                            months = ['January', 'February', 'March', 'April', 'May', 'June']
                            month = months.index(month1)
                            df = df[df['Start Time'].dt.month == month + 1]
                    except (KeyError, NameError, TypeError, ValueError):
                        print(" Oooops!\n Please use the appropriate name and begin with a capital letter (e.g. January)\n ")
                    else:
                        break

            elif filter_option == 'day':
                while True:
                    try:
                        day1 = input("Please enter a day of your choice. All days must begin with a capital letter. (e.g. Monday)\n")
                        # filter by day of week if applicable
                        if day1 != 'both':
                            # filter by day of week to create the new dataframe
                            days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                            day = days.index(day1)
                            df = df[df['Start Time'].dt.day == day + 1]
                    except (KeyError, NameError, TypeError, ValueError):
                        print(" Oooops!\n Please use the appropriate name and begin with a capital letter (e.g. Monday)\n ")
                    else:
                        break

            elif filter_option == 'both':
                while True:
                    try:
                        month1 = input("Please choose a month between January and June. Ensure to begin with a 'Capital letter'.(e.g. January)\n")
                    except (KeyError, NameError, TypeError, ValueError):
                        print(" Oooops!\n Please use the appropriate name and begin with a capital letter (e.g. January)\n ")
                    else:
                        break
                while True:
                    try:
                        day1 = input("Please enter a day of your choice. All days must begin with a capital letter. (e.g. Monday)\n")
                    except (KeyError, NameError, TypeError, ValueError):
                        print(" Oooops!\n Please use the appropriate name and begin with a capital letter (e.g. Monday)\n ")
                    else:
                        break
                    if (month1 or day1) != 'all':
                        months = ['January', 'February', 'March', 'April', 'May', 'June']
                        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                        month = months.index(month1)
                        day = days.index(day1)
                        df = df[(df['Start Time'].dt.month == month + 1) & (df['Start Time'].dt.day == day + 1)]
            else:
                print(" Oooops!\n Please use the appropriate name and begin with a lower case (e.g. month, day or both) ")
                if (filter_option not in filter_words):
                    continue


        except (KeyError, NameError, TypeError, ValueError):
            print(" Oooops!\n Please use the appropriate name and begin with a lower case (e.g. month, day or both) ")
            if (filter_option not in filter_words):
                continue
        else:
            break
    return df
df = load_data('city', 'month', 'day')
print("Here is the data statistics you have requested for....")
# print value counts for each user type
user_types = pd.Series(df['User Type'].value_counts())
print("This is the user analysis \n{} :".format(user_types))

print("computing the next data statistics.....")

# extract hour of week from Start Time to create new columns
df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
Most_popular_hour = pd.DataFrame(df['hour']).mode()

print("The Most common hour is \n{} ".format(Most_popular_hour))

print("computing the next data statistics.....")

# extract day from the Start Time column to create a day column
df['day'] = pd.DatetimeIndex(df['Start Time']).day_name()
# find the most common day (from 0 to 23)
popular_day = pd.DataFrame(df['day']).mode()

print("The Most Frequent Start Day of week:\n{} ".format(popular_day))

print("computing the next data statistics.....")
# extract month and day of week from Start Time to create new columns
df['month'] = pd.DatetimeIndex(df['Start Time']).month_name()
Most_popular_month = pd.Series(df['month']).mode()

print("The Most common month is:\n{}".format(Most_popular_month))

print("computing the next data statistics.....")

Most_popular_station = pd.Series(df['Start Station']).mode()

print("The most common start station is:\n{}".format(Most_popular_station))

print("computing the next data statistics.....")

Most_popular_end_station = pd.Series(df['End Station']).mode()

print("The most common end station is:\n{}".format(Most_popular_end_station))
print("computing the next data statistics.....")

Most_popular_trip_duration = pd.Series(df['Trip Duration']).mode()
print("The most common Trip duration are:\n{}".format(Most_popular_trip_duration))

print("computing the next data statistics.....")
df['day_of_week1'] = pd.DatetimeIndex(df['Start Time']).day_name()
bb = df['day_of_week1'].mode()
print("The most common day of the week is :\n{} ".format(bb))

print("processing the next data....")

columns = ['Start Station', 'End Station']
df1 = pd.DataFrame(df[:], columns=columns).mode()

print("The most common trip from start to end is :\n{} ".format(df1))

print("processing the next data....")

Total_duration = np.sum(df['Trip Duration'])
Average_Total_duration = np.mean(df['Trip Duration'])
print("The total trip duration is:{} and the average of the durations is : {}".format(Total_duration, Average_Total_duration))
print("processing the next data....")

Gender_counts = pd.Series(df['Gender'].value_counts())
print("This is the count according to the gender:\n {}".format(Gender_counts))
print("processing the next data....")

Most_common_Birth_year = pd.Series(df['Birth Year']).mode()
print("The most common birth year is:\n ", Most_common_Birth_year)

(a,b) = (0,5)
while True:
    if b>df.shape[0]:
        b = df.shape[0]+1
    print(df.iloc[a:b,:])
    a+=5
    if a>df.shape[0]:
        break
    b+=5
    CD = input("Do you want more data?\n Enter yes or no\n").lower().strip()
    if CD == 'no':
        break
