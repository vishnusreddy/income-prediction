import pandas as pd

#Reading the dataset
df = pd.read_csv("./input/adult.csv")

#Making ? as nan
from numpy import nan
df = df.replace('?', nan)

#Now dropping all NaN
df = df.dropna()
df['income']=df['income'].map({'<=50K': 0, '>50K': 1})

#Saving as a CSV file
df.to_csv('./input/without-grouping.csv', header=True, index=False) 

#Now grouping the data
my_df=df.copy()

#Grouping the education column values
my_df['education'].replace('Preschool', 'dropout',inplace=True)
my_df['education'].replace('10th', 'dropout',inplace=True)
my_df['education'].replace('11th', 'dropout',inplace=True)
my_df['education'].replace('12th', 'dropout',inplace=True)
my_df['education'].replace('1st-4th', 'dropout',inplace=True)
my_df['education'].replace('5th-6th', 'dropout',inplace=True)
my_df['education'].replace('7th-8th', 'dropout',inplace=True)
my_df['education'].replace('9th', 'dropout',inplace=True)
my_df['education'].replace('HS-Grad', 'HighGrad',inplace=True)
my_df['education'].replace('HS-grad', 'HighGrad',inplace=True)
my_df['education'].replace('Some-college', 'CommunityCollege',inplace=True)
my_df['education'].replace('Assoc-acdm', 'CommunityCollege',inplace=True)
my_df['education'].replace('Assoc-voc', 'CommunityCollege',inplace=True)
my_df['education'].replace('Bachelors', 'Bachelors',inplace=True)
my_df['education'].replace('Masters', 'Masters',inplace=True)
my_df['education'].replace('Prof-school', 'Masters',inplace=True)
my_df['education'].replace('Doctorate', 'Doctorate',inplace=True)

#Grouping the marital-status column
my_df['marital-status'].replace('Never-married', 'NotMarried',inplace=True)
my_df['marital-status'].replace(['Married-AF-spouse'], 'Married',inplace=True)
my_df['marital-status'].replace(['Married-civ-spouse'], 'Married',inplace=True)
my_df['marital-status'].replace(['Married-spouse-absent'], 'NotMarried',inplace=True)
my_df['marital-status'].replace(['Separated'], 'Separated',inplace=True)
my_df['marital-status'].replace(['Divorced'], 'Separated',inplace=True)
my_df['marital-status'].replace(['Widowed'], 'Widowed',inplace=True)

#Grouping the workclass
my_df['workclass'].replace('Federal-gov','Government', inplace=True)
my_df['workclass'].replace('Local-gov','Government', inplace=True)
my_df['workclass'].replace('State-gov','Government', inplace=True)
my_df['workclass'].replace('Self-emp-inc','Self-Employed', inplace=True)
my_df['workclass'].replace('Self-emp-not-inc','Self-Employed', inplace=True)
my_df['workclass'].replace('Unknown','Other', inplace=True)

my_df.to_csv('./input/with-grouping.csv', header=True, index=False)
