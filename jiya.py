#===============================================================================
# 11. VISUALIZATION
#===============================================================================
plt.figure()
plt.scatter(Y_test, Y_pred)
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Charges")
plt.show()

#===============================================================================
# 12. FEATURE IMPORTANCE
#===============================================================================
importances = model.feature_importances_

feature_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print("\nFeature Importance:\n", feature_df)

#===============================================================================
# 13. FINAL CONCLUSION
#===============================================================================
print("\n--------------------Final Conclusion-------------------------\n")

# Show actual performance
print(f"Model R2 Score: {r2:.4f}")
print(f"Cross Validation Score: {cv_scores.mean():.4f}")
