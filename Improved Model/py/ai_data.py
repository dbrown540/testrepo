import pandas as pd

# Read csv file
df = pd.read_csv('predicted_ai_data.csv', delimiter=',')

df.drop(['Unnamed: 2'], axis=1, inplace=True)

df.to_excel('predicted_ai_data.xlsx', sheet_name='predicted_ai_data', index=False)

