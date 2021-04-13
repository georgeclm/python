import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
dataset = pd.read_csv('SalesJan2009.csv')
head_data = dataset.head(10)
plt.figure(figsize=(15, 5))
plt.bar(head_data['Product'], head_data['City'])
plt.show()
# matplotlib.use('tkagg')
# print('Covid-1 Cases in 1 Week:\n')
# plt.bar([1, 2, 3, 4, 5, 6, 7], [10, 30, 10, 20, 100, 50, 40])
# plt.ylabel('(Label Y) Death Cases')
# plt.xlabel("(Label X) Day-")
# plt.show()
