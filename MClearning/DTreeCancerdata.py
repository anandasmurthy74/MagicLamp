import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import pydotplus
import io
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import misc
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA


def show_tree(tree, features, path):
    f = io.StringIO()
    export_graphviz(tree, out_file=f, class_names=['malignant','benign'], feature_names=features, impurity=False)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams['figure.figsize'] = (20, 20)
    plt.imshow(img)

def visualize_corr_hist(df):
    df.hist()
    plt.xticks()
    plt.show()

def visualize_scatter_matrix(df):
    scatter_matrix(df, alpha=0.2,figsize=(30,30), diagonal='kde')
    plt.xticks(rotation=30)
    plt.yticks(rotation=30)
    plt.show()

def visualize_density_plot(df, title, label):
    plt.figure(title)
    df.plot(kind='density', layout=(8,8), label=label)
    plt.show()

def visualize_pca_analysis(df):
    pca = PCA(n_components=2).fit(df)
    print("Explained variance : ",pca.explained_variance_ratio_)
    print("Explained variance sum : ",pca.explained_variance_ratio_.sum() )

    pca_2d = pca.transform(df)
    plt.figure('Wisconsin Breast Cancer Diagnostic Dataset')
    plt.title('PCA')
    plt.scatter(pca_2d[:,0], pca_2d[:,1], c=np.asarray(df['Type']))
    df.corr().plot.kde(title='PCA')
    plt.show()


cancer = load_breast_cancer()
df = pd.DataFrame.from_dict(cancer['data'])
df.columns=cancer['feature_names']
df['Type']=cancer['target']
temp_df = df.corr()
print(df.shape)
print(cancer.feature_names)
# print(temp_df.describe())
visualize_corr_hist(temp_df)
# visualize_density_plot(temp_df,'Feature Density plot',"Feature_density")
visualize_pca_analysis(df)

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
# tree = DecisionTreeClassifier(max_depth=4,min_samples_split=14, random_state=4)
tree = RandomForestClassifier(max_depth=4,min_samples_split=14, random_state=4)
tree.fit(X_train, y_train)
print("Accuracy :", tree.score(X_test, y_test))
# show_tree(tree, cancer.feature_names, "dttree.png")

