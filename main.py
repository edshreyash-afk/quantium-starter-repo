import pandas as pd
from pathlib import Path

# Load all CSV files
data_path = Path("data")
csv_files = list(data_path.glob("*.csv"))

df_list = [pd.read_csv(file) for file in csv_files]

# Combine into one DataFrame
df = pd.concat(df_list, ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Clean price column
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required fields
final_df = df[["sales", "date", "region"]]

# Save output file
output_path = Path("formatted_sales.csv")
final_df.to_csv(output_path, index=False)

print("Formatted output saved to:", output_path)
print("\nSample output:")
print(final_df.head())
