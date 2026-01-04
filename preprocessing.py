import pandas as pd
from dbconnection import load_data

df = load_data()

df['EMI_income_ratio'] = df['loan_amount'] / (df['income'] * 12)

X = df.drop(['loan_id', 'default_status'], axis=1)
y = df['default_status']


print(X.head())
