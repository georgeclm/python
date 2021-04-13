import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('worldometer_data.csv')
tail_data = dataset.tail(10)
plt.figure(figsize=(20, 5))
plt.bar(tail_data['Country/Region'], tail_data['TotalRecovered'])
plt.ylabel('Total Recovered(People)')
plt.xlabel('Country/Region')
plt.savefig('theres.jpg')
# plt.show()
