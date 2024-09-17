import pandas as pd

# Load the data and handle quoted fields
df = pd.read_csv('players.csv', quotechar='"')

# Preview the first few rows
df.head()
# Drop rows with missing data
df_cleaned = df.dropna()

# Check if there are any remaining missing values
print(df_cleaned.isnull().sum())

# Convert birth_date to datetime
df_cleaned['birth_date'] = pd.to_datetime(df_cleaned['birth_date'])

from datetime import datetime

# Calculate age from birth_date
current_year = datetime.now().year
df_cleaned['age'] = current_year - df_cleaned['birth_date'].dt.year

# Ensure wage and performance metrics are numeric
df_cleaned['wage_euro'] = pd.to_numeric(df_cleaned['wage_euro'], errors='coerce')
df_cleaned['overall_rating'] = pd.to_numeric(df_cleaned['overall_rating'], errors='coerce')
df_cleaned['value_euro'] = pd.to_numeric(df_cleaned['value_euro'], errors='coerce')

# Check the data types of the cleaned dataframe
print(df_cleaned.dtypes)

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('clean_players.csv', index=False)
