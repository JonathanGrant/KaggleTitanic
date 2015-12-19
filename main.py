#https://www.kaggle.com/c/titanic/details/getting-started-with-python
import csv as csv
import numpy as np

file = csv.reader(open('train.csv','rb'))
header = file.next()
data = []
for row in file:
    data.append(row)
data = np.array(data)