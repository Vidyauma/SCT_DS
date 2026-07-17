# Titanic Data Cleaning and Exploratory Data Analysis (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("train.csv")

# -----------------------------
# Display First 5 Rows
# -----------------------------
print("First 5 Rows:")
print(df.head())

# -----------------------------
# Dataset Information
# -----------------------------
print("\nShape of Dataset:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------

# Fill Age with Median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill Embarked with Mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin Column
df.drop('Cabin', axis=1, inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# Survival Count
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()

# -----------------------------
# Gender vs Survival
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Gender vs Survival')
plt.show()

# -----------------------------
# Passenger Class vs Survival
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Passenger Class vs Survival')
plt.show()

# -----------------------------
# Age Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# -----------------------------
# Fare Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.show()

# -----------------------------
# Fare vs Survival
# -----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare vs Survival')
plt.show()

# -----------------------------
# Age vs Survival
# -----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival')
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(10, 7))
sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# -----------------------------
# Survival Percentage
# -----------------------------
survival_percentage = (
    df['Survived'].value_counts(normalize=True) * 100
)

print("\nSurvival Percentage:")
print(survival_percentage)

# -----------------------------
# Findings
# -----------------------------
print("\n----- Findings -----")
print("1. Females survived more than males.")
print("2. First-class passengers had higher survival rates.")
print("3. Higher fare passengers survived more.")
print("4. Most passengers were between 20 and 40 years old.")
print("5. Third-class passengers had the highest death rate.")