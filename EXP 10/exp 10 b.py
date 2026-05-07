import matplotlib.pyplot as plt

# Data for visualization
names = ["A", "B", "C", "D"]
marks = [80, 75, 90, 85]

# 1. Bar Chart
plt.bar(names, marks)
plt.title("Bar Chart - Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Line Chart
plt.plot(names, marks, marker='o')
plt.title("Line Chart - Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart - Marks Distribution")
plt.show()