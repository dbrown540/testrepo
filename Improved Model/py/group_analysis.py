import pandas as pd

# Read the JSON data into a DataFrame
df = pd.read_json('statistics_basic_filter_groups.json', orient='index')
df = df.reset_index().rename(columns={'index': 'Topic'})

# Reshape the DataFrame
df = df.melt(id_vars=['Topic'], var_name='Group', value_name='Counts')
df[['TP', 'FP', 'FN']] = pd.DataFrame(df['Counts'].tolist())

# Select the desired columns
df = df[['Topic', 'Group', 'TP', 'FP', 'FN']]

# Save the DataFrame to Excel
df.to_excel('group_statistics.xlsx', sheet_name='statistics_basic_filter_groups', index=False)