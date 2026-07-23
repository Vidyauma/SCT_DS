# ==========================================
# SkillCraft Data Science Internship - Task 3
# Decision Tree Classifier
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("output", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("bank.csv")

print("=" * 50)
print("First 5 Rows")
print("=" * 50)
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# Encode Categorical Columns
# ==========================================

label_encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = label_encoder.fit_transform(df[column])

# ==========================================
# Features and Target
# ==========================================

X = df.drop("deposit", axis=1)
y = df["deposit"]

# ==========================================
# Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================================
# Train Decision Tree
# ==========================================

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================================
# Prediction
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("Model Accuracy")
print("=" * 50)
print(f"Accuracy : {accuracy * 100:.2f}%")

# ==========================================
# Confusion Matrix
# ==========================================

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No", "Yes"]
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")

plt.savefig(
    "output/confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# Decision Tree
# ==========================================

plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No", "Yes"],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Decision Tree Classifier")

plt.savefig(
    "output/decision_tree.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# Feature Importance
# ==========================================

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nFeature Importance:")
print(importance)

plt.figure(figsize=(10, 7))

importance.plot(kind="bar")

plt.title("Feature Importance")

plt.xlabel("Features")

plt.ylabel("Importance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "output/feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "=" * 50)
print("Project Completed Successfully!")
print("=" * 50)
print("Generated Files:")
print("1. output/confusion_matrix.png")
print("2. output/decision_tree.png")
print("3. output/feature_importance.png")