import pandas as pd
import numpy as np

# Creating the dataset
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, 75, None, 90, 85],
    "Age": [20, 21, 19, None, 22]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Cleaning the data by dropping rows with missing values
df_clean = df.dropna()

print("\nCleaned Data:")
print(df_clean)

print("\nSummary Statistics:")
print(df_clean.describe())