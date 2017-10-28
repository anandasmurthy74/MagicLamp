import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.cluster import KMeans
from pandas.plotting import radviz
from sklearn import decomposition
from sklearn.decomposition import PCA

df = pd.read_csv('AvayaApplist_rawdata.csv')

temp_df = df.copy()
temp_df.drop(['CI Name', 'App Type', 'Usage'], axis=1, inplace=True)
temp_df.dropna(inplace=True)
temp_df.replace(to_replace=['Cloud'], value=[9], inplace=True)
temp_df.dropna(inplace=True)
temp_df = temp_df.apply(pd.to_numeric)
X = np.array(temp_df)

a = decomposition.PCA(n_components=3)

pca_a = a.fit(X)

print("Explained variance ratio : ", pca_a.explained_variance_ratio_)
print("Explained variance ratio cumulative", pca_a.explained_variance_ratio_.sum())

pca = PCA(n_components=2).fit(temp_df)
pca_2d = pca.transform(temp_df)

clf = KMeans(n_clusters=6)
clf.fit(X)

print(type(clf.labels_))
print(clf.labels_)
# plt.figure('Avaya Applications grouping - 6 clusters')
# plt.scatter(pca_2d[:,0], pca_2d[:,1], c = clf.labels_)
# plt.show()



