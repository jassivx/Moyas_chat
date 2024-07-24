import pandas as pd
import numpy as np

# Define the path to the combined CSV file and the output SQL file
csv_file_path = 'F://combined_data.csv'
sql_file_path = 'F://combined_data2.sql'

# Define the table name (change this to your desired table name)
table_name = 'your_table_name'

# Read the combined CSV file into a DataFrame
df = pd.read_csv(csv_file_path, low_memory=False)

# Open the SQL file in write mode
with open(sql_file_path, 'w', encoding='utf-8') as sql_file:
    # Write the SQL header for creating the table (modify this according to your schema)
    sql_file.write(f"CREATE TABLE {table_name} (\n")
    for col in df.columns:
        sql_file.write(f"    {col} TEXT,\n")  # Modify this based on your data types
    sql_file.write(");\n\n")

    # Generate and write the INSERT statements
    for index, row in df.iterrows():
        sql_file.write(f"INSERT INTO {table_name} (")
        sql_file.write(", ".join(df.columns))
        sql_file.write(") VALUES (")
        values = []
        for value in row.values:
            if pd.isna(value):  # Handle None or NaN values
                values.append("NULL")
            elif isinstance(value, str):  # Handle string values
                escaped_value = value.replace("'", "''")  # Escape single quotes
                values.append(f"'{escaped_value}'")
            elif isinstance(value, int):  # Handle integer values
                values.append(str(value))
            elif isinstance(value, float):  # Handle float values
                if np.isnan(value):  # Handle NaN values in float columns
                    values.append("NULL")
                else:
                    # Format float with appropriate precision
                    values.append(str(value))
            else:
                values.append("NULL")  # Default to NULL for unexpected types
        sql_file.write(", ".join(values))
        sql_file.write(");\n")

print(f"SQL file has been written to {sql_file_path}")
