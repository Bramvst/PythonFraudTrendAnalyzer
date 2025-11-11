import pandas as pd
import joblib

def main():
    # Laad model
    model_path = "Models/fraude_random_forest.pkl"
    model = joblib.load(model_path)

    # Laad dataset (zorg dat je Data/creditcard.csv hebt)
    data_path = "Data/creditcard.csv"
    df = pd.read_csv(data_path)

    # Drop target column als die er is
    if "Class" in df.columns:
        X = df.drop(columns=["Class"])
    else:
        X = df.copy()

    # Voorspel
    predictions = model.predict(X)

    # Toon eerste 10 voorspellingen
    print("First 10 predictions:")
    print(predictions[:10])

if __name__ == "__main__":
    main()
