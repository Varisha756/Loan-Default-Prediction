from dbconnection import load_data

df = load_data()

df['EMI_income_ratio'] = df['loan_amount'] / (df['income'] * 12)

df.to_csv("loan_dashboard_data.csv", index=False)

print("CSV exported successfully")
