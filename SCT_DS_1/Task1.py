import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("world_population.csv")

# =========================
# 1. TOP 5 ROWS (TABLE STYLE)
# =========================
print("\n================ TOP 5 COUNTRIES ================\n")
print(df.head().to_string(index=False))

# =========================
# 2. DATASET INFO (CLEAN FORMAT)
# =========================
print("\n================ DATASET INFO ================\n")
info_df = pd.DataFrame({
    "Column": df.columns,
    "Non-Null Count": df.notnull().sum().values,
    "Data Type": df.dtypes.values
})
print(info_df.to_string(index=False))

# =========================
# 3. STATISTICAL SUMMARY (TABLE)
# =========================
print("\n================ STATISTICAL SUMMARY ================\n")
print(df.describe().to_string())

# =========================
# 4. MISSING VALUES (TABLE)
# =========================
print("\n================ MISSING VALUES ================\n")
missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})
print(missing_df.to_string(index=False))

# =========================
# 5. TOP 10 COUNTRIES (TABLE)
# =========================
print("\n================ TOP 10 POPULATED COUNTRIES (2022) ================\n")

top10 = df.sort_values(by="2022 Population", ascending=False).head(10)[
    ["Country/Territory", "Continent", "2022 Population"]
]

print(top10.to_string(index=False))

# =========================
# 6. CONTINENT SUMMARY (TABLE)
# =========================
print("\n================ COUNTRIES BY CONTINENT ================\n")

continent_df = df["Continent"].value_counts().reset_index()
continent_df.columns = ["Continent", "Number of Countries"]

print(continent_df.to_string(index=False))

# =========================
# 7. GRAPHS (STILL INCLUDED)
# =========================

# Top 10 bar chart
plt.figure(figsize=(12,6))
sns.barplot(
    data=df.sort_values(by="2022 Population", ascending=False).head(10),
    x="2022 Population",
    y="Country/Territory",
    hue="Country/Territory",
    palette="viridis",
    legend=False
)
plt.title("Top 10 Most Populated Countries (2022)")
plt.show()

# Histogram
plt.figure(figsize=(10,6))
plt.hist(df["2022 Population"], bins=30, edgecolor="black")
plt.title("Population Distribution (2022)")
plt.show()

# Continent chart
plt.figure(figsize=(10,6))
sns.barplot(
    x=continent_df["Number of Countries"],
    y=continent_df["Continent"],
    palette="coolwarm"
)
plt.title("Countries by Continent")
plt.show()