coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})
coefficients.sort_values(by="Coefficient", ascending=False)
