#Introduction
#Though there are a number of ways you can go about tackling this project, we recommend using NumPy and pandas. Using these libraries is the industry standard for working with data in Python. In the quizzes in this and the following sections, you will get some practice using NumPy and pandas to complete different parts of the project. Then for the project, you will need to piece your code together with some additional code to complete a final project! These sections will likely be helpful if you use NumPy and pandas to complete the project.

#Understanding the Data
#Let's use pandas to better understand the bike share data! Use this code editor to explore chicago.csv and answer the questions below. The file included here is a mini version of one of the actual data files you will work with for the project. It only includes 400 rows, but the structure and columns are the same.

#1. What columns are in this dataset?
#2. Are there any missing values?
#3. What are the different types of values in each column?
#4. Some useful pandas methods:

#df.head()
#df.columns
#df.describe()
#df.info()
#df['column_name'].value_counts()
#df['column_name'].unique()


import pandas as pd

df = pd.read_csv("chicago.csv")
print(df.head())  # start by viewing the first few rows of the dataset!