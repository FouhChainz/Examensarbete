import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the weather and dishes data into pandas DataFrames
weather_df = pd.read_csv("weather_main.csv")
dishes_df = pd.read_csv("dishes_main.csv")

# Merge the two DataFrames on the date column
merged_df = pd.merge(weather_df, dishes_df, on='date')

# Convert the "date" column to a pandas datetime object
merged_df['date'] = pd.to_datetime(merged_df['date'], format='%Y-%m-%d')

# Set the "date" column as the index of the DataFrame
merged_df = merged_df.set_index('date')

# Group the data by month and calculate the sum of the "sold" column for each month
monthly_sales = merged_df.resample('M').sum()

# Split the data into training and testing sets
train_data = monthly_sales[:-9]
test_data = monthly_sales[-3:]

# Train a linear regression model on the training data
model = LinearRegression()
model.fit(train_data[['temp']], train_data['sold'])

# Make predictions on the testing data
predictions = model.predict(test_data[['temp']])

# Calculate the mean squared error of the predictions
mse = mean_squared_error(test_data['sold'], predictions)

# Plot the actual and predicted sales on a graph
plt.plot(monthly_sales.index, monthly_sales['sold'], label='Actual Sales')
plt.plot(test_data.index, predictions, label='Predicted Sales')
plt.legend()
plt.show()

# Calculate and plot the residuals of the predictions
residuals = test_data['sold'] - predictions
plt.plot(test_data.index, residuals, label='Residuals')
plt.legend()
plt.show()