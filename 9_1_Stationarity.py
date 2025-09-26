# Forecasting: Principles and Practice
# 9 ARIMA models
# 9.1 Stationarity and differencing

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

gafa_stock = pd.read_csv("C:\Codigos\Libro_Forecasting\data\gafa_stock.csv", parse_dates=["ds"])

google = gafa_stock.query(
    "unique_id == 'GOOG_Close' and ds.dt.year == 2015"
).reset_index()
fig = plt.figure()

gs = fig.add_gridspec(1, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])

plot_acf(google["y"], ax=ax1, zero=False,
         title="Google closing stock price",
         bartlett_confint=False,
         auto_ylims=True)
plot_acf(
    google["y"].diff()[1:],
    ax=ax2,
    zero=False,
    title="Changes in Google closing stock price",
    bartlett_confint=False,
    auto_ylims=True
)

plt.show()