import numpy as np
import pandas as pd

print("--- NumPy Implementation ---")
# Create a 1D and 2D array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4]])

print(f"1D Array: {arr1}")
print(f"Mean of Array: {np.mean(arr1)}")
print(f"Square Root of Elements: {np.sqrt(arr1)}")

print("\n--- Pandas Implementation ---")
# Create a dictionary to convert into a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

print("DataFrame Content:")
print(df)
print(f"\nAccessing 'Name' Column:\n{df['Name']}")