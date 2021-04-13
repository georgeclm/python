import numpy as np
from sklearn.preprocessing import MinMaxScaler
from numpy import genfromtxt
data = genfromtxt('even_featurescaling.csv', delimiter=',')


print(data)
# Use feature_range named argument to scale it to a different scale. e.g
scaler = MinMaxScaler(feature_range=(0, 10))
# scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
print(scaled)
