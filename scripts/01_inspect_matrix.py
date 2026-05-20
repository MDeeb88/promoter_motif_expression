import pandas as pd
from pathlib import Path

matrix_path = Path("data/processed/motif_matrices/promoter_motif_M_woTFTPM0.csv")

print(f"Reading: {matrix_path}")
df = pd.read_csv(matrix_path, nrows=5)

print("\nShape preview:")
print(df.shape)

print("\nColumns:")
print(df.columns[:20].tolist())

print("\nFirst rows:")
print(df.head())
