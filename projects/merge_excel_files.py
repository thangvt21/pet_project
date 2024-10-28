import pandas as pd
import os

directory = (
    "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\logging\\web_payment@flashship.net\\"
)

sheet_name_to_merge = "Sheet1"

files = [f for f in os.listdir(directory) if f.endswith(".xlsx")]

dfs = []

for file in files:
    file_path = os.path.join(directory, file)
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name_to_merge, engine="openpyxl")
        dfs.append(df)
    except ValueError as e:
        print(f"Sheet '{sheet_name_to_merge}' not found in file '{file}'.")

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_excel(
    "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\logging\\web_payment@flashship.net\\web_payment@flashship.net_full.xlsx",
    index=False,
    engine="openpyxl",
)

print("Excel sheets merged successfully!")
