import numpy as np
from sklearn.preprocessing import MinMaxScaler
from numpy import genfromtxt
np.set_printoptions(precision=5)
data = genfromtxt('even_featurescaling.csv', delimiter=',')

print('Before Scaling:')
print(data)
print('\n')
# Use feature_range named argument to scale it to a different scale. e.g
scaler = MinMaxScaler(feature_range=(0, 10))
# scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
print('After Scaled:')
print(scaled)
