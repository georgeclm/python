# even student id
import numpy as np
import pandas as pd
dataset = pd.read_csv('./SacramentocrimeJanuary2006.csv')
print(f'The shape of the dataset is (rows,columns): {dataset.shape}\n')
print(f'The summary: \n{dataset.describe()}\n')
print(f'The columns of this dataset:\n{dataset.columns}\n')
print(f'The last 5 rows: \n {dataset.tail()}')
