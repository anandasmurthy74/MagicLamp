import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
from pandas.plotting import scatter_matrix
from itertools import cycle

df = pd.read_excel('C:\Anand\Opp\EMEA\ME\OSN\Data\Ticket_data.xlsx')
df.set_index('Request ID', inplace=True)
temp_df = df.copy()
temp_df['Impact'].replace(to_replace='Not Assigned', value=99, inplace=True)
temp_df['Impact'].replace(to_replace='4.Affects User', value=4, inplace=True)
temp_df['Impact'].replace(to_replace='2.Affects Group', value=2, inplace=True)
temp_df['Impact'].replace(to_replace='3.Affects Department', value=3, inplace=True)
temp_df['Impact'].replace(to_replace='1.Affects Business', value=1, inplace=True)

temp_df['Urgency'].replace(to_replace='Not Assigned', value=99, inplace=True)
temp_df['Urgency'].replace(to_replace='1.Critical', value=1, inplace=True)
temp_df['Urgency'].replace(to_replace='2.High', value=2, inplace=True)
temp_df['Urgency'].replace(to_replace='3.Medium', value=3, inplace=True)
temp_df['Urgency'].replace(to_replace='4.Low', value=4, inplace=True)
temp_df['Urgency'].replace(to_replace='VIP', value=2, inplace=True)

temp_df['subc_code'].fillna(11, axis=0,inplace=True)
temp_df['item_code'].fillna(2,axis=0, inplace=True)
temp_df.drop(['Request Mode', 'Technician', 'Group','Requester', 'Department', 'Subcategory', 'Item', 'Subject', 'Created By'], axis=1, inplace=True)
temp_df.dropna(thresh=3,inplace=True)

print(temp_df.describe())

#plt.figure(1)
#temp_df.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
#scatter_matrix(temp_df)
temp_df_var = temp_df.corr()
#temp_df_var.plot.kde()
# temp_df_var.plot(kind='kde', layout=(8,8), label='Variance plot')
# plt.figure('Radial distribution of K Means cluster along Spend per Employee')
# radviz(temp_df_var,'EC_code')

plt.show()
