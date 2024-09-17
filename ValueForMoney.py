import pandas as pd

# Load the cleaned data
df = pd.read_csv('clean_players.csv')

# Calculate the value for money metric
df['value_for_money'] = df['overall_rating'] / df['wage_euro']

# Save the results to a new file
df.to_csv('players_with_value_for_money.csv', index=False)

# Optional: Print out some results to verify
print(df[['full_name', 'overall_rating', 'wage_euro', 'value_for_money']].head())
