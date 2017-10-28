import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import numpy as np
import pandas as pd 
import graphviz
import pydotplus
import io
from scipy import misc
from sklearn.metrics import accuracy_score

def show_tree(tree, features, path):
	f = io.StringIO()
	export_graphviz(tree, out_file=f,feature_names=features)
	pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
	img = misc.imread(path)
	plt.rcParams['figure.figsize']=(20,20)
	plt.imshow(img)


# X = np.array([(1,8,50),(2,15,75),(3,35,103),(6,60,101),(7,80,150),(8,85,103),(10,95,101)])
# Y = np.array([1,0,1,1,4,5,6])
features =['Age', "Weight"]
X = np.array([(1,8),(2,15),(3,35),(6,60),(7,80),(8,85),(10,95), (12, 75) , (14, 90), (17, 87), (20,95)])
y = np.array([1,0,1,1,1,0,0,0,0,1,1])


clf = tree.DecisionTreeClassifier()
# clf = svm.SVC(gamma=0.0001, C=100)
clf.fit(X,y)
show_tree(clf,features, "dttree.png")

myset =  [(4,25), (9,95), (25,135)]
out = clf.predict(myset)
print('prediction : ',out )
