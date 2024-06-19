# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px
import os

# Define the target directory where the CSV files are located
target_directory = r'E:\Git\Unicorn Dashboard Analysis'
file_extension = '.csv'

# Loop through the files in the target directory and print the paths of CSV files
for dirname, _, filenames in os.walk(target_directory):
    for filename in filenames:
        if filename.endswith(file_extension):
            print(os.path.join(dirname, filename))

# Load the dataset
df = pd.read_csv(r'E:\Git\Unicorn Dashboard Analysis\List of Unicorns in the World.csv')

# Basic DataFrame operations to understand the dataset structure and content
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())
#print(df.duplicated().sum())

# Extract the year from the 'Date Joined' column
df['year'] = pd.DatetimeIndex(df['Date Joined']).year

# Dropping an unnamed column that might be an index column from the CSV
df.drop(columns=['Unnamed: 0'], inplace=True)

# Analysis on number of unicorns by country
unicorn_country = df['Country'].value_counts().reset_index()

# Convert valuation strings to float for numeric operations
df['Valuation ($B)'] = df['Valuation ($B)'].str.replace('$', '').str.replace(',', '').astype(float)

# Grouping companies by valuation
company_valuation = (df.groupby('Company')['Valuation ($B)'].sum().reset_index()).sort_values(by='Valuation ($B)', ascending=False)

# Analyzing valuation by country
country_valuation = (df.groupby('Country')['Valuation ($B)'].sum().reset_index()).sort_values(by='Valuation ($B)', ascending=False).reset_index().drop(columns='index')

# Analyzing valuation over the years
valuation_by_year = (df.groupby('year')['Valuation ($B)'].sum().reset_index()).sort_values(by='Valuation ($B)', ascending=False)

# Finding the company with maximum and minimum valuation
# print(df.loc[df['Valuation ($B)'].idxmax()])
# print(df.loc[df['Valuation ($B)'].idxmin()])

# Analysis on the distribution of industries among unicorns
industry = df['Industry'].value_counts().reset_index()

# Grouping industries by their total valuation
industry_valuation = (df.groupby('Industry')['Valuation ($B)'].sum().reset_index()).sort_values(by='Valuation ($B)', ascending=False)

# Creating a strip plot using Plotly Express to visualize valuation by year, colored by country
fig = px.strip(data_frame=df, x='year', y='Valuation ($B)', color='Country', log_y=True, height=1200, hover_name='Company')
fig.show()