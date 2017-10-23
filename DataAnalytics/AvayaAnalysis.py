import pandas as pd
from pandas.plotting import radviz
import matplotlib.pyplot as plt
from matplotlib import style


df = pd.read_csv('AvayaApplist_rawdata.csv')

temp_df = df.copy()
temp_df.drop(['CI Name', 'App Type', 'Usage'], axis=1, inplace=True)


temp_df.dropna(inplace=True)
temp_df.replace(to_replace=['Cloud'], value=[9], inplace=True)


temp_df = temp_df.apply(pd.to_numeric)
temp_df_var = temp_df.var()


#print(temp_df_var.head())
temp_df_var.plot.barh(colormap='Greens')
# plt.figure()
# radviz(temp_df_var, 'Interfaces')
plt.show()
