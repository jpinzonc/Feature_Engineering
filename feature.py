#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
ds1 = pd.read_csv('North_Texas_Companies.csv')
ds2 = pd.read_csv('2010_Census_Population.csv')

# Munge and Merge Data
ds1 = ds1.rename(columns={'Primary Zip': 'Zip'})
ds2 = ds2.rename(columns={'Zip Code ZCTA': 'Zip'})
ds= pd.merge(ds1,ds2, on='Zip')
ds = ds.rename(columns={'Revenue (US Dollars, million)': 'Revenue', '2010 Census Population': 'Population'})
ds['Revenue'] = ds['Revenue'] * 1000000
ds['Revenue_Per_Person'] = ds['Revenue'] / ds['Population']
