import pandas as pd

# Load the Master.xlsx file
master_df = pd.read_excel('Master(1).xlsx')

# Convert the 'Date' column to datetime format
master_df['Date'] = pd.to_datetime(master_df['Date'])

# Extract month and year from the 'Date' column
master_df['Month'] = master_df['Date'].dt.strftime('%b')
master_df['Year'] = master_df['Date'].dt.year

# Group by 'Month' and 'Year' and transpose the columns
output_df = master_df.groupby(['Month', 'Year']).agg({'A': 'sum', 'B': 'sum', 'C': 'sum'}).unstack()

# Reorder the columns to match the desired output
output_df = output_df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]

# Save the output to Output.xlsx
output_df.to_excel('Output(1).xlsx')

print("Output(1).xlsx file has been created successfully.")
