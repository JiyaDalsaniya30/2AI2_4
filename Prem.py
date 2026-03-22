#===============================================================================
# 3. DATA PREPROCESSING
#===============================================================================

# Handle missing values
print("\n---------------Missing Values------------\n", df.isnull().sum())

# Convert categorical variables using One-Hot Encoding
df = pd.get_dummies(df, drop_first=True)

print("\nAfter Encoding:\n", df.head())

#===============================================================================
# 4. FEATURE ENGINEERING (BOOST ACCURACY)   
#===============================================================================

# Create new meaningful features
df['bmi_age'] = df['bmi'] * df['age']
df['smoker_bmi'] = df['bmi'] * df['smoker_yes']     