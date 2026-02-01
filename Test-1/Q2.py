# encoding_utils.py 
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

def apply_encodings(df, target_col):
    # 1. One-Hot Encoding [cite: 18]
    df_ohe = pd.get_dummies(df, columns=['category_col_1'])
    
    # 2. Label Encoding [cite: 19]
    le = LabelEncoder()
    df['cat_label'] = le.fit_transform(df['category_col_2'])
    
    # 3. Ordinal Encoding [cite: 20]
    oe = OrdinalEncoder()
    df['cat_ordinal'] = oe.fit_transform(df[['education_level']])
    
    # 4. Frequency Encoding [cite: 21]
    freq = df['category_col_3'].value_counts(normalize=True)
    df['cat_freq'] = df['category_col_3'].map(freq)
    
    # 5. Target Encoding [cite: 22]
    target_mean = df.groupby('category_col_4')[target_col].mean()
    df['cat_target'] = df['category_col_4'].map(target_mean)
    
    return df