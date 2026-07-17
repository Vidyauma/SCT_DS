# Titanic Data Cleaning and Exploratory Data Analysis (EDA) 🚢

## 📌 Project Overview

This project focuses on performing **Data Cleaning** and **Exploratory Data Analysis (EDA)** on the Titanic dataset.

The main goal of this project is to analyze passenger information and identify the factors that influenced survival during the Titanic disaster.

The project includes:
- Data loading and exploration
- Handling missing values
- Data preprocessing
- Data visualization
- Statistical analysis
- Extracting insights from the dataset

---

## 📂 Dataset

**Dataset Name:** Titanic Dataset (`train.csv`)

The dataset contains passenger details such as:

| Feature | Description |
|---|---|
| PassengerId | Unique passenger identification number |
| Survived | Survival status (0 = No, 1 = Yes) |
| Pclass | Passenger class |
| Name | Passenger name |
| Sex | Gender of passenger |
| Age | Passenger age |
| SibSp | Number of siblings/spouses aboard |
| Parch | Number of parents/children aboard |
| Ticket | Ticket number |
| Fare | Ticket fare |
| Cabin | Cabin number |
| Embarked | Port of embarkation |

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Tools
- Visual Studio Code
- GitHub

---

## 📁 Project Structure

```
Titanic_EDA
│
├── train.csv
│
├── task2.py
│
├── requirements.txt
│
├── README.md
│
└── output
    │
    ├── survival_count.png
    ├── gender_vs_survival.png
    ├── passenger_class_vs_survival.png
    ├── age_distribution.png
    ├── fare_distribution.png
    ├── fare_vs_survival.png
    ├── age_vs_survival.png
    └── correlation_heatmap.png
```

---

# ⚙️ Installation and Setup

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

## Step 2: Navigate to Project Folder

```bash
cd Titanic_EDA
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the Python file:

```bash
python task2.py
```

The program performs:

1. Dataset loading
2. Data exploration
3. Missing value handling
4. Data cleaning
5. Visualization generation
6. Insight extraction

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

### Missing Value Handling

- Checked missing values using Pandas.
- Filled missing **Age** values using the median.
- Filled missing **Embarked** values using the mode.

### Feature Removal

- Removed the **Cabin** column because it contained many missing values.

### Data Validation

- Verified that missing values were handled after cleaning.

---

# 📊 Exploratory Data Analysis

## 1. Survival Analysis

Analyzed the number of passengers who survived and did not survive.

**Visualization:**
- Survival Count Plot


## 2. Gender vs Survival

Compared survival rates between male and female passengers.

**Observation:**
- Female passengers had a higher survival rate.


## 3. Passenger Class vs Survival

Analyzed survival based on passenger class.

**Observation:**
- First-class passengers had better survival chances.
- Third-class passengers had higher death rates.


## 4. Age Distribution

Studied the age distribution of passengers.

**Observation:**
- Most passengers were between 20 and 40 years old.


## 5. Fare Analysis

Analyzed ticket fare distribution and its relationship with survival.

**Observation:**
- Passengers with higher fares showed better survival probability.


## 6. Correlation Analysis

Generated a correlation heatmap to identify relationships between numerical features.

---

# 📈 Visualizations

The project generates the following plots:

| Visualization | Purpose |
|---|---|
| Survival Count | Shows survived vs deceased passengers |
| Gender vs Survival | Compares survival by gender |
| Passenger Class vs Survival | Analyzes class impact |
| Age Distribution | Shows passenger age pattern |
| Fare Distribution | Shows fare variation |
| Fare vs Survival | Compares fare impact |
| Age vs Survival | Studies age relationship |
| Correlation Heatmap | Shows feature relationships |

---

# 🔍 Key Findings

- Female passengers had a higher survival rate than male passengers.
- First-class passengers had a greater chance of survival.
- Higher fare passengers showed better survival probability.
- Most passengers belonged to the 20–40 age group.
- Passenger class and gender were important survival factors.

---

# 🚀 Future Improvements

Possible improvements:

- Apply Machine Learning algorithms for survival prediction.
- Perform feature engineering.
- Compare classification models.
- Build an interactive dashboard using Power BI.
- Deploy the model using Streamlit.

---

# 💡 Skills Demonstrated

- Python Programming
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Statistical Analysis
- Data Interpretation
- Pandas Data Processing
- Matplotlib & Seaborn Visualization

---

# 👩‍💻 Author

**Vidya S**

B.E Computer Science and Engineering (2026)

### Skills

Python | SQL | Power BI | Excel | Machine Learning | Data Analytics | Java | AI

---

⭐ If you found this project useful, feel free to explore and connect.