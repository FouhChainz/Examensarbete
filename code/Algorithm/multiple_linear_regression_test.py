import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("/Users/christianzhaco/Skola/PycharmProjects/Examensarbete/code/data_totaled.csv")
# Replace any string values in the 'sold' column with NaN values

# Convert the 'sold' column to a numeric type
# Replace the "−" sign with "-"
df['temp'] = df['temp'].str.replace('−', '-')

# Convert the "temperature" column to numerical values
df['temp'] = pd.to_numeric(df['temp'], errors='coerce')


# Make sure the index column is in a datetime format
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Drop any rows with NaN values
df = df.dropna()
# Split the data into training and testing sets
train_data = df[:273]
test_data = df[92:]

# Extract the features and target columns
features = ['temp'
    , 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4', 'weekday_5', 'weekday_6', 'weekday_7'
    , 'weather_status_Klart', 'weather_status_Moln', 'weather_status_Regn', 'weather_status_Snö']

target = 'sold'

# Fit a multiple linear regression model on the training data
reg = LinearRegression().fit(train_data[features], train_data[target])

# Use the model to make predictions on the test data
predictions = reg.predict(test_data[features])

# Calculate the mean squared error and root mean squared error
mse = mean_squared_error(test_data[target], predictions)
rmse = np.sqrt(mse)

# Print the MSE and RMSE
print('MSE:', mse)
print('RMSE:', rmse)
print(predictions)

# Plot the predicted sales vs actual sales
plt.plot(df.index,df['sold'], label="Sålda")
plt.plot(test_data.index,predictions, label="Prediktion")
plt.xlabel("Datum")
plt.ylabel("Antal sålda rätter")
plt.title("Sålda vs Förutspådd Försäljning")
plt.legend()
plt.show()
