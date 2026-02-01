Missing Values: Median imputation was chosen for numerical columns like LotFrontage because it is less sensitive to extreme outliers than the mean. Mode was used for categorical data to preserve the most frequent category.

Categorical Encoding: One-Hot Encoding was best for nominal features with few categories (like MSZoning). Ordinal Encoding was essential for quality features (like ExterQual) to preserve their natural rank. Target Encoding handled high-cardinality features like Neighborhood efficiently without adding 25+ columns.

Feature Scaling: Standardization (Z-score) was the most effective because many house features (like GrLivArea) approximate a normal distribution, and many ML algorithms assume zero mean and unit variance.

Outliers & Skewness: Log transformation on SalePrice was critical as the original distribution was highly right-skewed; this transformation stabilized the variance and made the distribution more symmetric for better model performance.
