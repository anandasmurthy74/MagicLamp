import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import svm
import graphviz
import pydotplus
import io
from scipy import misc
from sklearn.metrics import accuracy_score

age = pd.Series(np.random.randint(1, 10, 500), name='age')
height = pd.Series(np.random.randint(75, 130, 500), name='height_cms')
weight = pd.Series(np.random.randint(12, 100, 500), name='height_cms')
label = pd.Series(np.random.randint(0,2, 50), name='x') 

df = pd.DataFrame()

df1 = pd.concat([df,age, height, weight, label], axis=1)

print(df1.head())
