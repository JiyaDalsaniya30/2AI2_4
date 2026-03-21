#===============================================================================
# (Dhruv Mahajan)
# MODEL EVALUATION
#===============================================================================

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

#===============================================================================
# 9. MODEL EVALUATION
#===============================================================================

mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("\nModel Performance:")
print("Mean Squared Error:", mse)
print(f"R2 Score: {r2:.2f}")

#===============================================================================
# 10. CROSS VALIDATION
#===============================================================================

cv_scores = cross_val_score(model, X, Y, cv=10, scoring='r2')

print("\nCross Validation R2 Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())