import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35],'city': ['New York', 'Los Angeles', 'Chicage']}

df = pd.DataFrame(data)
print("dataFrame:\n",df)

average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

filtered_df = df[df['Age'] > 28]
print("\nFiltered DataFrame (age > 28):\n:", filtered_df)

df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with Salary column:\n", df)