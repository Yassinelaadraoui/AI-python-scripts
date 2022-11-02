import pandas as pd
from matplotlib import pyplot as plt

# Load data from a text file
df_students = pd.read_csv(r'C:\Users\Dell\Desktop\gdpByCountry.csv',delimiter=',',header=0)

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

fig = plt.figure(figsize=(10,4))

# Plot density
df_students["2018"].plot.density()

# Add titles and labels
plt.title('Data Density')

# Show the mean, median, and mode
#plt.axvline(x=df_students["2018"].mean(), color = 'cyan', linestyle='dashed', linewidth = 2)
#plt.axvline(x=df_students["2018"].median(), color = 'red', linestyle='dashed', linewidth = 2)
#plt.axvline(x=df_students["2018"].mode()[0], color = 'yellow', linestyle='dashed', linewidth = 2)

# Show the figure
#plt.show()
plt.bar(x=df_students["Country Name"], height=df_students["2018"])
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0)
plt.xticks(rotation=90)

plt.show()

