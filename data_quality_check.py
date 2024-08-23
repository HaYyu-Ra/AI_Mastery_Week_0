missing_values = df.isnull().sum()
print(missing_values)

# Checking for outliers
outliers = df[(df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)]
print(outliers)
