import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the weather and dishes data
weather_data = pd.read_csv("/Users/christianzhaco/PycharmProjects/Examensarbete/data/weather_main.csv")
dishes_data = pd.read_csv("/Users/christianzhaco/PycharmProjects/Examensarbete/data/dishes_main.csv")

# Merge the two datasets on the date column
data = pd.merge(weather_data, dishes_data, on='date')

# Extract the input and target variables
X = data[['temp']]
y = data['sold']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the linear regression model on the training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Use the trained model to make predictions on the test data
y_pred = regressor.predict(X_test)

# Evaluate the performance of the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2: {r2}")

# Use the trained model to make predictions on future data
future_weather = pd.DataFrame({'temp': [30, 25, 20, 18, 15]})
future_predictions = regressor.predict(future_weather)
print(f"Future Sales Predictions: {future_predictions}")

plt.figure()
plt.plot()
plt.plot(future_predictions)
plt.xlabel("date")
plt.ylabel("sold")
plt.show()
