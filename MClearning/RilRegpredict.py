import pandas as pd 
import quandl, math
import numpy as np 
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = pd.read_csv('NSE-SUZLON.csv')

df = df [['Open', 'High', 'Low', 'Close', 'Total Trade Quantity']]

df ['HL_PCT'] = (df['High'] - df['Low'])/df['Low'] * 100
df['PCT_change'] = (df['Open'] - df['Close'])/df['Close'] * 100

df = df[['Close', 'HL_PCT','PCT_change', 'Total Trade Quantity']]

forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.3 * len(df)))
print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)


X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X = preprocessing.scale(X,1)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
#clf = svm.SVR()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
y_pred = clf.predict(X_test)
count = 0
for x in range(0, len(y_pred)):
	var = (y_test[x] - y_pred[x]) 
	if var < 0:
		var = var * -1

	if (var) <= 10:
		print(y_test[x], ' ', math.ceil(y_pred[x]))
		count+=1
print(count/len(y_pred) * 100 , '%')



