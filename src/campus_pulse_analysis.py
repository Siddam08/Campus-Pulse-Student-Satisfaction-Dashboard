# =========================================
# Campus Pulse – Student Satisfaction Analysis
# Python + Pandas + Matplotlib + Seaborn
# =========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
data_path = "../data/campus_pulse_raw.csv"
df = pd.read_csv(data_path)

print("\nInitial Data Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -----------------------------
# 2. Check Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 3. Data Cleaning
# -----------------------------
# Convert Rating to numeric
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Remove rows with missing important fields
df_cleaned = df.dropna(subset=['Department', 'Facility', 'Rating'])

print("\nCleaned Data Info:")
print(df_cleaned.info())

# -----------------------------
# 4. Basic Statistics
# -----------------------------
print("\nBasic Statistics:")
print(df_cleaned['Rating'].describe())

# -----------------------------
# 5. Analysis
# -----------------------------

# Average rating by Facility
avg_facility = df_cleaned.groupby('Facility')['Rating'].mean().reset_index()

# Average rating by Department
avg_department = df_cleaned.groupby('Department')['Rating'].mean().reset_index()

# Feedback count by Department
dept_count = df_cleaned['Department'].value_counts().reset_index()
dept_count.columns = ['Department', 'Feedback Count']

print("\nAverage Rating by Facility:")
print(avg_facility)

print("\nAverage Rating by Department:")
print(avg_department)

print("\nFeedback Count by Department:")
print(dept_count)

# -----------------------------
# 6. Visualization (Python)
# -----------------------------

# Chart 1: Average Satisfaction by Facility
plt.figure(figsize=(8, 5))
sns.barplot(data=avg_facility, x='Facility', y='Rating', palette='Blues_d')
plt.title("Average Satisfaction Rating by Facility")
plt.xlabel("Facility")
plt.ylabel("Average Rating")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Chart 2: Average Satisfaction by Department
plt.figure(figsize=(8, 5))
sns.barplot(data=avg_department, x='Department', y='Rating', palette='Greens_d')
plt.title("Average Satisfaction Rating by Department")
plt.xlabel("Department")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# -----------------------------
# 7. Save Cleaned Dataset
# -----------------------------
output_path = "../data/campus_pulse_cleaned.csv"
df_cleaned.to_csv(output_path, index=False)

print("\n Cleaned data saved successfully at:", output_path)
