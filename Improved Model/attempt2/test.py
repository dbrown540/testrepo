import pandas as pd

# Load the JSON file
data = pd.read_json('/Users/developer/Desktop/Coding/Work/InsightsAI/Improved Model/json/statistics_basic_filter_groups.json')

# Create empty lists to store the extracted data
topics = []
groups = []
true_positives = []
false_positives = []
false_negatives = []

# Iterate over the data dictionary and extract the values
for topic, groups_dict in data.items():
    for group, values in groups_dict.items():
        topics.append(topic)
        groups.append(group)
        true_positives.append(values['tp'])
        false_positives.append(values['fp'])
        false_negatives.append(values['fn'])

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'Topic': topics,
    'Group': groups,
    'True Positive': true_positives,
    'False Positive': false_positives,
    'False Negative': false_negatives
})

# Count the number of true positives for each group
total_true_positive = df.groupby('Group')['True Positive'].sum()

# Count the number of false positives for each group
total_false_positive = df.groupby('Group')['False Positive'].sum()

# Count the number of false negatives for each group
total_false_negative = df.groupby('Group')['False Negative'].sum()

# Create the summary DataFrame
summary_df = pd.DataFrame({
    'True Positive': total_true_positive,
    'False Positive': total_false_positive,
    'False Negative': total_false_negative
})

print(summary_df)
