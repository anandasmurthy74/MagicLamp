import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv('AvayaApplist_rawdata.csv')

temp_df = df.copy()
temp_df.drop(['CI Name', 'App Type', 'Usage'], axis=1, inplace=True)
temp_df.dropna(inplace=True)
temp_df.replace(to_replace=['Cloud'], value=[9], inplace=True)
temp_df.dropna(inplace=True)
temp_df = temp_df.apply(pd.to_numeric)

temp_df_var = temp_df.corr()

#temp_df_var.plot.barh(colormap='Greens')
temp_df.hist()
temp_df_var.hist()
plt.show()

