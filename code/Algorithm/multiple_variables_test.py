import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/data/sales_data.csv')

# Clean and prepare the data
df.dropna(inplace=True)
df = pd.get_dummies(df, columns=['weekday', 'weather_status'])
df['temp'] = pd.to_numeric(df['temp'],errors='coerce')
df = df[['date', 'sold', 'temp', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4', 'weekday_5', 'weekday_6', 'weekday_7', 'weather_status_Klart', 'weather_status_Moln','weather_status_Regn', 'weather_status_Snö']]
df.dropna(inplace=True)

# Split the data into training and testing sets
X = df.drop(columns=['date', 'sold'])
y = df['sold']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Evaluate the model
y_pred = regressor.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"Y predict: {y_pred}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R^2 Score: {r2}")

# Make predictions
future_data = np.array([[2023, 2, 10, 72, 0, 0, 0, 0, 0, 1, 0, 0]])
future_sales = regressor.predict(future_data)
print(f"Predicted Sales for 2023-02-10: {future_sales}")

plt.plot(df.index, df[ 'sold' ], label='Actual')
plt.plot(y_pred, label='Predicted')
plt.xlabel("date")
plt.ylabel("sold")
plt.legend()
plt.show()

