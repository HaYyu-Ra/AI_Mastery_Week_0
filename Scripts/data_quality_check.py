# Check for missing values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

# Check for outliers
outliers = df[(df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)]
print("Outliers:\n", outliers)
