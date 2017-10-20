import pandas as pd

wine = pd.read_csv("winequality-red.csv")


print(wine.describe())