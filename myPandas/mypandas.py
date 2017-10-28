import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import radviz


Applist = pd.read_excel("C:/Anand/Opp/NA/Avaya/Avaya Raw data.xlsx")
# writer = pd.ExcelWriter("Correlation.xlsx")
# df2= Applist.corr()
# df2_stat = df2.describe()
# df2.to_excel(writer,'Sheet2')

print(Applist.columns)
# plt.figure()
#radviz(Applist, 'COTS Rating ')

print(Applist.head())

print(Applist.prod())