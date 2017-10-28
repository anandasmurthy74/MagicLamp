import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from pandas.plotting import radviz
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import AffinityPropagation
from sklearn import decomposition
from sklearn.decomposition import PCA
from itertools import cycle
import seaborn as sb

base_dir='C:/Anand/MagicLamp/DataAnalytics/datafiles/'
file_avaya_app= 'AvayaApplist_rawdata.csv'
file_ncr_app = 'NCR_app_list_numeric.xlsx'
file_osn_app = 'OSN_Application_data.xlsx'
file_osn_tickets = 'OSN_Ticket_data.xlsx'
df1 = pd.read_csv(base_dir+file_avaya_app, delimiter='\t')
df2 = pd.read_excel(base_dir+file_ncr_app)
df3 = pd.read_excel(base_dir+file_osn_app)
df4 = pd.read_excel(base_dir+file_osn_tickets)

frames = [df1,df2,df3,df4]
temp_df = df1.append([df2,df3])

writer = pd.ExcelWriter(base_dir+'Out.xls')
temp_df.to_excel(writer, sheet_name="Apps_data")
writer.save()
print(temp_df.shape)