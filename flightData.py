import pandas as pd
from matplotlib import pyplot as plt

# Load data from a text file
flights = pd.read_csv(r'C:\Users\Dell\Desktop\flights.csv',delimiter=',',header=0)

# Remove any rows with missing data
flights = flights.dropna(axis=0, how='any')

print(flights)


