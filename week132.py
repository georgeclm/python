import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
dataset = pd.read_csv('even_labelencoder.csv')
desa_df = pd.DataFrame(dataset, columns=['desa'])
labelencoder = LabelEncoder()
desa_df['Desa_Cat'] = labelencoder.fit_transform(
    desa_df['desa'])
print(desa_df)
