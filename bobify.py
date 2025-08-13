import pandas as pd
import xlsxwriter

# Define all columns from the goals_import_v3 template exactly as they appear
template_columns = [
    'Email *Required',
    'Objective *Required\n*Goal name',
    'Status *Required\n*On Track, Off Track, Completed, Incomplete, Other',
    'Visibility *Required\n*Personal, Shared',
    'Description\n*Goal description',
    'Aligned to\n*Custom type or company goal name',
    'Time frame *Required\nPrevious quarter, This quarter, This half, Next quarter, Previous year, This year, Next year, Date range',
    'Date range\nStart date\n *if applicable\n*Use the date format of your local site',
    'Date range\nEnd date\n *if applicable\n*Use the date format of your local site',
    'Tags'
]

# Append key result-related columns (up to 48)
for i in range(1, 49):
    template_columns.extend([
        f'Key result {i}',
        f'Measure key result {i} by\n*Values: Percentage, Numeric, Currency, Complete/Incomplete',
        f'Currency Target {i}\n*if applicable\n*e.g. 1000, $1000, 1000 USD',
        f'Numeric Target {i}\n*if applicable\n*More than or equal to 0'
    ])

# Create the output DataFrame with all columns
output_df = pd.DataFrame(columns=template_columns)

# Read goals from the external CSV file with the new columns
try:
    goals_df = pd.read_csv(
        'goals_input.csv'
    )
except FileNotFoundError:
    print("Error: 'goals_input.csv' not found. Please create the file with the data provided.")
    exit()

# Group key results by email, goal, and timeframe
grouped_goals = goals_df.groupby([
    'Email',
    'GoalName',
    'Timeframe'
])['KeyResult'].apply(list)

# Populate the output DataFrame
for (email, goal, timeframe), key_results in grouped_goals.items():
    new_row = pd.Series(dtype='object')

    # Populate the main goal columns from the provided data
    new_row['Email *Required'] = email
    new_row['Objective *Required\n*Goal name'] = goal
    new_row['Time frame *Required\nPrevious quarter, This quarter, This half, Next quarter, Previous year, This year, Next year, Date range'] = timeframe

    # Set the static values for Status and Visibility
    new_row['Status *Required\n*On Track, Off Track, Completed, Incomplete, Other'] = 'On Track'
    new_row['Visibility *Required\n*Personal, Shared'] = 'Personal'

    # Populate the key result columns and their measure columns
    for i, key_result in enumerate(key_results):
        if i < 48:
            new_row[f'Key result {i+1}'] = key_result
            new_row[f'Measure key result {i+1} by\n*Values: Percentage, Numeric, Currency, Complete/Incomplete'] = 'Percentage'
        else:
            print(f"Warning: Goal '{goal}' has more than 48 key results. The rest will be ignored.")
            break
    
    # Append the new row to the output DataFrame
    output_df = pd.concat([output_df, pd.DataFrame([new_row])], ignore_index=True)

# Save the output to a new Excel file
output_df.to_excel('goals_import_v3_bob.xlsx', index=False)
print("Conversion complete. Output saved to 'goals_import_v3_bob.xlsx'")