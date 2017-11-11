import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import load_breast_cancer
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd 
import graphviz
import pydotplus
import io
from scipy import misc
from sklearn.metrics import accuracy_score

def show_tree(tree, features, path):
	f = io.StringIO()
	export_graphviz(tree, out_file=f, class_names=['malignant', 'benign'], feature_names=features, impurity=False)
	pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
	img = misc.imread(path)

	plt.rcParams['figure.figsize'] =(20,20)
	plt.imshow(img)

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify =cancer.target, random_state=42)
tree = DecisionTreeClassifier(max_depth=6, min_samples_split=10, random_state=0)
tree.fit(X_train, y_train)

show_tree(tree, cancer.feature_names, "BreastCancer.png")
accuracy = tree.score(X_test, y_test)
print('Accuracy :', accuracy)