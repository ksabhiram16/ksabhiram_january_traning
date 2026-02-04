lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_pred = np.round(lr_pred)

print("Linear Regression Accuracy:", accuracy_score(y_test, lr_pred))
