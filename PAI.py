#===============================================================================
# 5. DEFINE FEATURES & TARGET
#===============================================================================
X = df.drop("charges", axis=1)
Y = df["charges"]

#===============================================================================
# 6. TRAIN-TEST SPLIT
#===============================================================================
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("\nTraining Size:", X_train.shape)
print("Testing Size:", X_test.shape)

