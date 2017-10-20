import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier 
from sklearn.cross_validation import train_test_split

data = pd.read_csv('mnist_test.csv')

df_x = data.iloc[:,1:]

df_y = data.iloc[:,0]
print("type : ",type(df_x), "df x '\n'", df_x)
p_df = pd.read_csv("hw_digit-2.csv", index_col=0)
print("type : ",type(p_df), "p df '\n'", p_df)

#x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.05, random_state=4)

# rf = RandomForestClassifier(n_estimators = 100)
# rf.fit(x_train, y_train)


#predict = rf.predict(p_df)

#print(predict)


# count = 0

# for s in range(len(y_test)):
# 	if predict[s] == (y_test.tolist())[s]:
# 		count+=1 
# print("Accuracy : ",count/len(y_test))
