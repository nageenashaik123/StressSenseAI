import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "data/StressLevelDataset.csv"
)

print("\nDataset Shape")
print(df.shape)

# -----------------------------
# Missing Values
# -----------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Duplicates
# -----------------------------

print("\nDuplicate Rows")
print(df.duplicated().sum())

# -----------------------------
# Data Types
# -----------------------------

print("\nData Types")
print(df.dtypes)

# -----------------------------
# Stress Level Distribution
# -----------------------------

print("\nStress Level Distribution")
print(
    df["stress_level"].value_counts()
)

# -----------------------------
# Descriptive Statistics
# -----------------------------

print("\nSummary Statistics")
print(
    df.describe()
)