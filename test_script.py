 import pandas as pd

try:
    df = pd.read_csv("dataset.csv")
    print("Dataset loaded successfully")
except Exception as e:
    print(f"Error loading dataset: {e}")

