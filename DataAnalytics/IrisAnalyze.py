import pandas as pd
from pandas.plotting import radviz
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 
from sklearn.cluster import KMeans 
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA



iris = load_iris()

pca = PCA(n_components=2).fit(iris.data)
pca_2d = pca.transform(iris.data)

print(pca_2d)
plt.figure('Reference Plot')

plt.scatter(pca_2d[:, 0], pca_2d[:,1], c = iris.target)
plt.show()


