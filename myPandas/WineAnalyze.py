import numpy as np 


wines = np.genfromtxt("winequality-red.csv", delimiter=';', skip_header =1)


wines = np.array(wines[1:], dtype= np.float)
int_wines = wines.astype(int)
print(wines.sum(axis=1))