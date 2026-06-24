import joblib
import pandas as pd

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    "models/random_forest_model.pkl"
)

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "data/feature_engineered_data.csv"
)

X = df.drop(
    columns=["stress_level"]
)

# -----------------------------
# Feature Importance
# -----------------------------

importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")

print(importance_df)

print("\nTop 10 Features\n")

print(
    importance_df.head(10)
)