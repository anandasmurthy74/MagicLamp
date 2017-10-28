import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
print(type(iris))
df = pd.DataFrame()
df = iris['data']
print(df[0:10,1])

