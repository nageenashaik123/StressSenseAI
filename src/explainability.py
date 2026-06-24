import pandas as pd
import joblib

model = joblib.load(
    "models/random_forest_model.pkl"
)


def get_top_features(df):

    feature_names = df.columns

    importances = model.feature_importances_

    feature_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances,
        "Value": df.iloc[0].values
    })

    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=False
    )

    top_features = []

    for _, row in feature_df.head(5).iterrows():

        top_features.append(
            {
                "feature": row["Feature"],
                "value": float(row["Value"]),
                "importance": round(
                    row["Importance"],
                    4
                )
            }
        )

    return top_features