

import pandas as pd

# Reading the first CSV file
try:
    df_total_final = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//total_final.csv')
    print("Dataframe 'total_final.csv' successfully created!")
    print(df_total_final.columns)
except FileNotFoundError:
    print("Error: File 'total_final.csv' not found!")
except pd.errors.ParserError:
    print("Error: Couldn't parse the CSV file 'total_final.csv'!")

# Reading the second CSV file
try:
    df_present_absent = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//present+absent.csv')
    print("Dataframe 'present+absent.csv' successfully created!")
    print(df_present_absent.columns)
except FileNotFoundError:
    print("Error: File 'present+absent.csv' not found!")
except pd.errors.ParserError:
    print("Error: Couldn't parse the CSV file 'present+absent.csv'!")

# Check if both dataframes were created successfully before merging
if 'df_total_final' in locals() and 'df_present_absent' in locals():
    # Merging the two dataframes on 'attn_id'
    merged_df = pd.merge(df_total_final, df_present_absent, on='Attn_id', how='left')

    # Display the merged dataframe
    print("Merged DataFrame:")
    print(merged_df)
else:
    print("Merging not possible. One or both DataFrames are not available.")

dff = merged_df.to_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn_result.csv')




'''

import pandas as pd

# Reading the first CSV file
try:
    df_total_final = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//total_final.csv')
    print("Dataframe 'total_final.csv' successfully created!")
    print(df_total_final.columns)
except FileNotFoundError:
    print("Error: File 'total_final.csv' not found!")
except pd.errors.ParserError:
    print("Error: Couldn't parse the CSV file 'total_final.csv'!")

# Reading the second CSV file
try:
    df_present_absent = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//present+absent.csv')
    print("Dataframe 'present+absent.csv' successfully created!")
    print(df_present_absent.columns)
except FileNotFoundError:
    print("Error: File 'present+absent.csv' not found!")
except pd.errors.ParserError:
    print("Error: Couldn't parse the CSV file 'present+absent.csv'!")

# Check if both dataframes were created successfully before merging
if 'df_total_final' in locals() and 'df_present_absent' in locals():
    # Check if 'Attn_id' exists in both dataframes
    if 'Attn_id' in df_total_final.columns and 'Attn_id' in df_present_absent.columns:
        # Merging the two dataframes on 'Attn_id'
        merged_df = pd.merge(df_total_final, df_present_absent, on='Attn_id', how='left')

        # Display the merged dataframe
        print("Merged DataFrame:")
        print(merged_df)

        # Save the merged dataframe to a new CSV file
        merged_df.to_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn_result.csv', index=False)
        print("Merged DataFrame saved to 'attn_result.csv'.")
    else:
        print("Error: 'Attn_id' column not found in one or both DataFrames.")
else:
    print("Merging not possible. One or both DataFrames are not available.")
'''