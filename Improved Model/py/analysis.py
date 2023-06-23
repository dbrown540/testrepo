import pandas as pd
import json

# Step 1: Read the JSON data into a DataFrame
df = pd.read_json('statistics_basic_filter_topics.json')

# Step 2: Reshape the DataFrame
df = df.stack().reset_index().rename(columns={'level_0': 'Category', 'level_1': 'Subcategory'})
df = pd.concat([df.drop([0], axis=1), df[0].apply(pd.Series)], axis=1).dropna()

# Step 3: Save the DataFrame to Excel
df.to_excel('statistics.xlsx', sheet_name="statistics_basic_filter_topics", index=False)