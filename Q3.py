"""
Scenario: Build progressively

    -read dataset (temperature sensors data)
    -understand dataset
    -plot data in various ways
        -supply voltage / conversion time
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "/Users/ep9k/Desktop/Python_GenAI-main/TemperatureSensorsData.xlsx"


# Load the Excel file and assign correct headers from row 5
df = pd.read_excel("TemperatureSensorsData.xlsx", sheet_name="Overview", engine="openpyxl", skiprows=5)

# Rename columns for easier access
df.columns = [
    "Paper Number", "Technology (nm)", "Area (mm²)", "Supply Voltage (V)", "Temperature Resolution (°C)",
    "Conversion Time (ms)", "Inaccuracy (°C)", "Calibration point", "Power (µW)",
    "Energy/Conversion (nJ)", "FOM (nJ/K²)"
]

# Convert relevant columns to numeric, coercing errors to NaN
df["Supply Voltage (V)"] = pd.to_numeric(df["Supply Voltage (V)"], errors='coerce')
df["Conversion Time (ms)"] = pd.to_numeric(df["Conversion Time (ms)"], errors='coerce')

# Drop rows with missing values in the required columns
df_clean = df.dropna(subset=["Supply Voltage (V)", "Conversion Time (ms)"])


# Plotting
plt.figure(figsize=(12, 8))
plt.scatter(df_clean["Supply Voltage (V)"], df_clean["Conversion Time (ms)"], color='blue')

# Label each point with its Paper Number
for i, row in df_clean.iterrows():
    plt.text(row["Supply Voltage (V)"], row["Conversion Time (ms)"], row["Paper Number"], fontsize=8, ha='right')

plt.title("Supply Voltage vs. Conversion Time with Paper Number Labels")
plt.xlabel("Supply Voltage (V)")
plt.ylabel("Conversion Time (ms)")
plt.grid(True)
plt.tight_layout()
plt.show()


