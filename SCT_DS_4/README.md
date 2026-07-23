# Traffic Accident Data Analysis

This project was completed as part of the **SkillCraft Technology Data Science Internship – Task 04**.

## Objective

The objective of this project is to analyze road accident data and understand accident patterns using Exploratory Data Analysis (EDA). Different visualizations are created to identify trends and compare accident statistics across different states.

## Dataset

- **Dataset Name:** Road-Accidents-2018-Annexure-13.csv
- The dataset contains state-wise road accident statistics for India.

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```
SCT_DS_4/
│
├── Road-Accidents-2018-Annexure-13.csv
├── task4.py
├── requirements.txt
├── README.md
└── output/
    ├── accidents_by_state.png
    ├── top10_states.png
    ├── accident_distribution.png
    ├── boxplot.png
    ├── correlation_heatmap.png
    └── pairplot.png
```

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the Python file:

```bash
python task4.py
```

## Analysis Performed

The program performs the following tasks:

- Loads the dataset
- Displays basic information about the dataset
- Checks for missing values
- Generates summary statistics
- Creates a correlation heatmap
- Visualizes total accidents by state
- Displays the top 10 states with the highest number of accidents
- Creates a histogram of accident counts
- Generates a boxplot for accident data
- Creates a pairplot for numeric features

## Output

All generated graphs are saved inside the **output** folder.

The output includes:

- accidents_by_state.png
- top10_states.png
- accident_distribution.png
- boxplot.png
- correlation_heatmap.png
- pairplot.png

## Conclusion

This project helped in understanding how Python can be used for data cleaning, analysis, and visualization. The charts provide a simple overview of accident statistics across different states and show relationships between numerical features in the dataset.

## Author

**Vidya S**

B.E. Computer Science and Engineering

SkillCraft Technology – Data Science Internship