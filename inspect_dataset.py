
import pandas as pd
from pathlib import Path

file_path = Path("data/flood_risk_dataset_india.csv")

if not file_path.exists():
    raise FileNotFoundError(f"Dataset not found: {file_path.resolve()}")

df = pd.read_csv(file_path)

print("\n--- DATASET SHAPE ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(df.head().to_string())

print("\n--- DATA TYPES ---")
print(df.dtypes.to_string())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum().to_string())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

target = "Flood Occurred"
if target in df.columns:
    print("\n--- TARGET DISTRIBUTION ---")
    print(df[target].value_counts(dropna=False).to_string())
else:
    print(f"\nWARNING: Target column '{target}' not found.")
