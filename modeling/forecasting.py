import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

def forecast_transactions(ts_csv="transactions.csv"):
    df = pd.read_csv(ts_csv, parse_dates=['date'], index_col='date')
    ts = df['count']

    # ARIMA model
    arima_model = ARIMA(ts, order=(1, 1, 1)).fit()
    arima_forecast = arima_model.forecast(steps=7)

    # Holt-Winters model
    hw_model = ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=7).fit()
    hw_forecast = hw_model.forecast(7)

    ts.plot(label="History")
    arima_forecast.plot(label="ARIMA Forecast")
    hw_forecast.plot(label="Holt-Winters Forecast")
    plt.legend()
    plt.title("Weekly Forecast")
    plt.show()

if __name__ == "__main__":
    print("Run with sample timeseries like 'date,count'")
