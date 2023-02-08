import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


def predict_dishes_sold(weather_file, dishes_file):
    # Load the data
    weather = pd.read_csv(weather_file)
    dishes = pd.read_csv(dishes_file)

    # Combine the data into one DataFrame
    df = pd.merge(dishes, weather, on='date', how='outer')

    # Convert date to datetime and set it as the index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    # Split the data into training and test sets
    df_train = df[:-90]
    df_test = df[-90:]

    # Train the model
    regressor = RandomForestRegressor()
    regressor.fit(df_train[['temp']], df_train['sold'])

    # Make predictions for the test set
    y_pred = regressor.predict(df_test[['temp']])

    # Plot the actual and predicted values
    plt.plot(df_test.index, df_test['sold'], label='Actual')
    plt.plot(df_test.index, y_pred, label='Predicted')
    plt.legend()
    plt.show()


predict_dishes_sold("weather_main.csv", "dishes_main.csv")
