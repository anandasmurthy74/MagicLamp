import pandas as pd

Applist = pd.read_excel("C:/Anand/Opp/NA/Avaya/Avaya Raw data.xlsx")
writer = pd.ExcelWriter("Correlation.xlsx")
df2= Applist.corr()
df2.to_excel(writer,'Sheet1')
