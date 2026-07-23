import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Create Output Folder
# -----------------------------
os.makedirs("output", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Dataset...\n")

df = pd.read_csv("Road-Accidents-2018-Annexure-13.csv")

print("Dataset Loaded Successfully!\n")

# -----------------------------
# Basic Information
# -----------------------------
print("Shape of Dataset:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Numeric Columns
# -----------------------------
numeric_df = df.select_dtypes(include="number")
numeric_columns = numeric_df.columns

print("\nNumeric Columns:")
print(numeric_columns.tolist())

# -----------------------------
# Correlation Heatmap
# -----------------------------
if len(numeric_columns) >= 2:
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("output/correlation_heatmap.png")
    plt.close()

# -----------------------------
# Accidents by State
# -----------------------------
state_column = df.columns[0]
accident_column = numeric_columns[-1]

state_accidents = (
    df.groupby(state_column)[accident_column]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(14, 7))
state_accidents.plot(kind="bar", color="steelblue")
plt.title("Total Accidents by State")
plt.xlabel("State")
plt.ylabel("Total Accidents")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("output/accidents_by_state.png")
plt.close()

# -----------------------------
# Top 10 States
# -----------------------------
top10 = state_accidents.head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top10.values, y=top10.index)
plt.title("Top 10 States with Highest Accidents")
plt.xlabel("Accidents")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("output/top10_states.png")
plt.close()

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(10, 6))
plt.hist(df[accident_column].dropna(), bins=20)
plt.title("Distribution of Accident Counts")
plt.xlabel("Accident Count")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/accident_distribution.png")
plt.close()

# -----------------------------
# Boxplot
# -----------------------------
plt.figure(figsize=(10, 5))
sns.boxplot(x=df[accident_column].dropna())
plt.title("Boxplot of Accident Counts")
plt.tight_layout()
plt.savefig("output/boxplot.png")
plt.close()

# -----------------------------
# Pairplot
# -----------------------------
print("\nCreating Pairplot...")

try:
    if len(numeric_columns) >= 2:

        sample_df = (
            numeric_df
            .dropna()
            .sample(
                n=min(500, len(numeric_df.dropna())),
                random_state=42
            )
        )

        g = sns.pairplot(sample_df)
        g.fig.suptitle("Pairplot of Numeric Features", y=1.02)
        g.savefig("output/pairplot.png")
        plt.close('all')

        print("Pairplot saved successfully.")

    else:
        print("Not enough numeric columns to create Pairplot.")

except Exception as e:
    print("Pairplot could not be created.")
    print("Reason:", e)

# -----------------------------
# Completed
# -----------------------------
print("\nAnalysis Completed Successfully!")
print("\nFiles Saved in 'output' Folder:")
print("✔ accidents_by_state.png")
print("✔ top10_states.png")
print("✔ accident_distribution.png")
print("✔ boxplot.png")
print("✔ correlation_heatmap.png")
print("✔ pairplot.png (if generated successfully)")