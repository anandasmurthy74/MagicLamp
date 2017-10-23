import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 
from sklearn.cluster import KMeans 
from sklearn import preprocessing
from sklearn.decomposition import PCA


df = pd.read_csv('AvayaApplist_rawdata.csv')

temp_df = df.copy()
temp_df.drop(['CI Name', 'App Type', 'Usage'], axis=1, inplace=True)
temp_df.dropna(inplace=True)
temp_df.replace(to_replace=['Cloud'], value=[9], inplace=True)
temp_df = temp_df.apply(pd.to_numeric)

pca = PCA(n_components=2).fit(temp_df)

pca_2d = pca.transform(temp_df)
X = np.array(temp_df)
print(X.shape)


clf = KMeans(n_clusters=5)
clf.fit(X)
#pca_labels = PCA(n_components=1).fit(clf.labels_)
#pca_1d = pca.tranform(pca_labels)
#print(pca_2d)
plt.figure('Avaya K Means with 6 clusters')
plt.scatter(pca_2d[:,0], pca_2d[:,1], c = clf.labels_)
plt.show()


# print(clf.cluster_centers_)
# print(clf.labels_)

# centroids = clf.cluster_centers_

# count = [0,0,0,0,0,0]
# for x in range(len(clf.labels_)-1):
# 	for y in range(0,5) :
# 		if clf.labels_[x] == y:
# 			count[y]+=1


# for x in range(0,5):
# 	print(count[x])

# x_axis = np.array(range(0,len(centroids)))

# print(x_axis)
# y_axis= np.array(count)
# print(y_axis)
# plt.scatter(x=x_axis, y=y_axis)
# plt.show()

