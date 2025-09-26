# Forecasting: Principles and Practice
# 9 ARIMA models
# 9.1 Stationarity and differencing

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

gafa_stock = pd.read_csv("C:/Codigos/data/gafa_stock.csv", parse_date=["ds"])