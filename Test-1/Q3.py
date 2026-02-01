from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, Normalizer, StandardScaler

# Prepare numerical data
X = df_cleaned[num_cols]

# 1. Min-Max Scaling [cite: 26]
X_minmax = MinMaxScaler().fit_transform(X)

# 2. Max Absolute Scaling [cite: 27]
X_maxabs = MaxAbsScaler().fit_transform(X)

# 3. Vector Normalization (L2) [cite: 29]
X_norm = Normalizer().fit_transform(X)

# 4. Z-score Standardization [cite: 30]
X_std = StandardScaler().fit_transform(X)