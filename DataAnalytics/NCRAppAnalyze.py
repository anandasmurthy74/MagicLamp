import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
from pandas.plotting import radviz
from itertools import cycle

df = pd.read_excel('NCR_app_list_numeric.xlsx')

temp_df = df.copy()
# dropped the text columns, and columns which are already considered in the derivative columns as indicators and scaled
temp_df.drop(['NCR Product', 'Industry', 'Category', 'Product Architecture/ Technology Stack','Total Spend', 'Potential Severance', 'High Cost', 'Low Cost', 'Total','H/M to L','Employee','Buffer (Contractors)', 'empspend' ], axis=1, inplace=True)
temp_df.dropna(inplace=True)
temp_df = temp_df.apply(pd.to_numeric)

temp_df_corr = temp_df.corr()

X= np.array(temp_df)
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=30)
print(bandwidth)
#clf = KMeans(n_clusters=5)
clf=MeanShift(bandwidth=bandwidth, bin_seeding=True)
clf.fit(X)
plt.figure(1)
temp_df_var = temp_df.corr()
temp_df_var.plot.hist(colormap='Greens')

labels = clf.labels_
cluster_centers = clf.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)
temp_df_var.plot(kind='kde', layout=(8,8), label='Variance plot')
plt.figure('Radial distribution of K Means cluster along Spend per Employee')
radviz(temp_df_var,'EC_code')


# plt.clf()
# plt.title('NCR Application clustering')

# colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# for k, col in zip(range(n_clusters_), colors):
#     my_members = labels == k
#     cluster_center = cluster_centers[k]
#     plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=14)
# plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

