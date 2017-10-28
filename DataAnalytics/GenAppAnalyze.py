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


def visualize_radial(df, col, title):
        plt.figure(title)
        radviz(df,col)
        plt.show()

def visualize_corr_hist(df, title):
    df.hist()
    plt.xticks()
    plt.show()

def visualize_corr_heatmap(df,title):
    sb.heatmap(df)
    plt.xticks(rotation=30)
    plt.yticks(rotation=30)
    plt.show()

def visualize_density_plot(df, title, label):
    plt.figure(title)
    df.plot(kind='density', layout=(8,8), label=label)
    plt.show()

# Visualizes the clusters using PCA
def visualize_clusters(clf, X,temp_df):
    # plt.clf()
    labels = clf.labels_
    cluster_centers = clf.cluster_centers_

    # project applist on to 2d using PCA
    X_pca = PCA(n_components=3).fit(X)
    X_pca2d = X_pca.transform(X)

    print("Explained variance : ",X_pca.explained_variance_ratio_)
    print("Explained variance sum : ",X_pca.explained_variance_ratio_.sum() )

    # project clusters to 2d using PCA
    Cluster_pca = PCA(n_components=2).fit(cluster_centers)
    Cluster_pca2d = Cluster_pca.transform(cluster_centers)

    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection = "3d")

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    print("number of estimated clusters : %d" % n_clusters_)

    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = Cluster_pca2d[k]
        ax1.scatter(X_pca2d[my_members, 0], X_pca2d[my_members, 1],X_pca2d[my_members, 2],col + '*')
        # plt.plot(X_pca2d[my_members, 0], X_pca2d[my_members, 1], col + '*', markersize=8)
        # plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=3)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()

def write_cluster_out(clf, orig_df):
    clusters_data = pd.DataFrame(clf.labels_)
    res_clusters = orig_df.join(clusters_data)
    res_clusters_temp = res_clusters
    res_clusters_temp['group'] = pd.to_numeric(np.array(clf.labels_))
    res_clusters_temp.set_index('CI Name', inplace=True)
    sort_col = ["group"]
    res_clusters_temp.sort_values(sort_col, inplace=True)
    out_cols = ['group', 'Criticality', 'App Type', 'Usage',
                'Brand Rating ', 'SOX Rating']
    out_df = res_clusters_temp[out_cols].copy()
    writer = pd.ExcelWriter("C:/Anand/Opp/NA/Avaya/Cluster_output.xlsx")
    out_df.to_excel(writer, sheet_name="Application Cluster data")
    writer.save()
    print("Output written to Excel")


df = pd.read_csv('C:\Anand\MagicLamp\DataAnalytics\AvayaApplist_rawdata.csv', delimiter='\t')
temp_df = df.copy()
# dropped the text columns, and columns which are already considered in the derivative columns as indicators and scaled
temp_df.drop(['CI Name', 'App Type', 'Usage'], axis=1, inplace=True)
# only for this dataset
temp_df.replace(to_replace=['Cloud'], value=[9], inplace=True)
temp_df.dropna(inplace=True)
temp_df = temp_df.apply(pd.to_numeric)
temp_df_corr = temp_df.corr()
X= np.array(temp_df)

#Apply the clustering algo - K Means or Meanshift
bandwidth = estimate_bandwidth(X, quantile=0.5, n_samples=135)
# clf = KMeans(n_clusters=5)
clf=MeanShift(bandwidth=bandwidth, bin_seeding=True)
# clf = AffinityPropagation(preference=-50)
clf.fit(X)

visualize_radial(temp_df,'Past 12 month Tickets Total', 'Radial Visual of Past 12 months ticket data')
visualize_corr_hist(temp_df_corr,"Feature Correlation Histogram")
visualize_corr_heatmap(temp_df_corr,"Feature Correlation Heatmap")
# visualize_clusters(clf,X, temp_df)
write_cluster_out(clf,df)