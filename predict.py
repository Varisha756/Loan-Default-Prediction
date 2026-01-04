new_data = [[30, 40000, 200000, 650, 3, 48, 13.5, 200000/(40000*12)]]
prediction = model.predict(new_data)

print("High Risk" if prediction[0] == 1 else "Low Risk")
