import pandas as pd
import numpy as np

stocks = pd.read_csv("data/Stock prices dataset.csv")
transactions = pd.read_csv("data/Financial Transaction Dataset.csv")

print(stocks.head())
print(stocks.info())

print(transactions.head())
print(transactions.info())