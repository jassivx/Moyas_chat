import pandas as pd

# Define the path to the Excel file and the output CSV file
excel_file_path = 'F://village list.xlsx'
csv_file_path = 'F://combined_data.csv'

# Read the Excel file to get the sheet names
xls = pd.ExcelFile(excel_file_path, engine='openpyxl')
sheet_names = xls.sheet_names

# Open the CSV file in write mode to write the header once
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    header_written = False
    for sheet in sheet_names:
        print(f"Reading sheet: {sheet}")
        # Read the entire sheet into a DataFrame
        df = pd.read_excel(excel_file_path, sheet_name=sheet, engine='openpyxl')

        # Process the DataFrame in smaller chunks if necessary
        chunk_size = 10000
        for start in range(0, df.shape[0], chunk_size):
            chunk = df.iloc[start:start + chunk_size]
            chunk.to_csv(csv_file, index=False, header=not header_written)
            header_written = True

print(f"Combined data has been written to {csv_file_path}")
