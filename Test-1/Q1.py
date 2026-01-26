import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

# 2. Data Cleaning & Preparation [cite: 10]
def clean_data(df):
    # Removing duplicate records [cite: 14]
    df = df.drop_duplicates()
    
    # Handling missing values [cite: 11]
    # Numerical: Median is often robust to outliers
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
        
    # Categorical: Mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Fixing incorrect data types [cite: 12]
    # Example: converting a 'Date' string to datetime
    # df['date_col'] = pd.to_datetime(df['date_col'])

    # Detecting and treating outliers (IQR Method) [cite: 13]
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.clip(df[col], lower_bound, upper_bound)
        
    # Dropping irrelevant features [cite: 15]
    # df = df.drop(['ID_column'], axis=1)
    
    return df

df_cleaned = clean_data(df)