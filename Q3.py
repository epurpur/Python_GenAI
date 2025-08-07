"""
Scenario: Build progressively

    -read dataset (temperature sensors data)
    -understand dataset
    ****Start here***-plot data in various ways
"""

import pandas as pd

# Load the Excel file
file_path = "/Users/ep9k/Desktop/Python_GenAI-main/TemperatureSensorsData.xlsx"

# Read the sheet and skip the first 6 rows to get to the actual data
df = pd.read_excel(file_path, sheet_name="Overview", engine="openpyxl", skiprows=6)

# Display the first few rows
print(df.head())
