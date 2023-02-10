import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Load the data
weather = pd.read_csv("/Users/christianzhaco/PycharmProjects/Examensarbete/data/weather_main.csv")
dishes = pd.read_csv("/Users/christianzhaco/PycharmProjects/Examensarbete/data/dishes_main.csv")

# Combine the data into one DataFrame
df=pd.merge(dishes, weather, on='date', how='outer')

# Convert date to datetime and set it as the index
df[ 'date' ]=pd.to_datetime(df[ 'date' ])
df=df.set_index('date')

# Split the data into training and test sets
df_train=df[ :-90 ]
df_test=df[ -90: ]

# Train the model
regressor=RandomForestRegressor()
regressor.fit(df_train[ [ 'temp' ] ], df_train[ 'sold' ])

# Make predictions for the test set
y_pred=regressor.predict(df_test[ [ 'temp' ] ])
print(df.head())
# Plot the actual and predicted values
plt.plot(df_test.index, df_test[ 'sold' ], label='Actual')
plt.plot(df_test.index, y_pred, label='Predicted')
plt.legend()
plt.show()

