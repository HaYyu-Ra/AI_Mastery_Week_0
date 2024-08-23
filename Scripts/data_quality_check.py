# Calculate and display the number of missing values in each column
missing_values_count = df.isnull().sum()
print(missing_values_count)

# Identify and display rows with outliers in GHI, DNI, or DHI columns
outliers = df[(df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)]
print(outliers)
