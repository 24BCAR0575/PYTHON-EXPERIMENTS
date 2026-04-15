import pandas as pd
import matplotlib.pyplot as plt

# 1. Prepare Data using Pandas
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [150, 200, 180, 250, 210]
}

df = pd.DataFrame(data)
print("Data for Plotting:")
print(df)

# 2. Visualize using Matplotlib
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', linestyle='--')

# Adding labels and title
plt.xlabel('Months of the Year')
plt.ylabel('Sales Figure')
plt.title('Monthly Sales Performance')

# Display the plot
plt.show()