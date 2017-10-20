import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 
from sklearn.cluster import KMeans 
from sklearn import preprocessing

style.use("ggplot")


df = pd.read_csv('AvayaApplist_rawdata.csv')

temp_df = df.copy()
temp_df.drop(['CI Name', 'App Type', 'Usage'], axis=1, inplace=True)


temp_df.dropna(inplace=True)
temp_df.replace(to_replace=['Cloud'], value=[9], inplace=True)


temp_df = temp_df.apply(pd.to_numeric)
X = np.array(temp_df)

#print(df.head())
clf = KMeans(n_clusters=6)
clf.fit(X)
# print(len(clf.cluster_centers_))
# print(clf.cluster_centers_)
# print(clf.labels_)

centroids = clf.cluster_centers_

count = [0,0,0,0,0,0]
for x in range(len(clf.labels_)-1):
	for y in range(0,5) :
		if clf.labels_[x] == y:
			count[y]+=1


for x in range(0,5):
	print(count[x])

x_axis = np.array(range(0,len(centroids)))

print(x_axis)
y_axis= np.array(count)
print(y_axis)
plt.scatter(x=x_axis, y=y_axis)
plt.show()

