#https://www.kaggle.com/c/titanic/details/getting-started-with-python
import time
import csv as csv
import numpy as np

start = time.time()

file = csv.reader(open('train.csv','rb'))
header = file.next()
data = []
for row in file:
    data.append(row)

#I want to use sciKit Learn svm
from sklearn import svm
clf = svm.SVC(verbose = 2, gamma = 0.001)

target = []
traindata = []
for dat in data:
    sex = 0
    if dat[4] == 'male':
        sex = 1
    traindata.append([float(dat[2]),
         float(dat[6]),
         float(dat[7]),
         float(dat[9]),
        sex])
    target.append(float(dat[1]))

clf.fit(traindata,target)

#Now open test file
test_file = csv.reader(open('test.csv','rb'))
header = test_file.next()

#Write a new file of predictions
predict_file = open('predict.csv','wb')
predict = csv.writer(predict_file)
predict_data = []

for row in test_file:
    predict_data.append(row)

for dat in predict_data:
    sex = 0
    if dat[3] == 'male':
        sex = 1
    try:
        predict.writerow(clf.predict([float(dat[1]),
                                       float(dat[5]),
                                       float(dat[6]),
                                       float(dat[8]),
                                      sex]))
    except:
        print dat


end = time.time()
print 'Total time elpased:', (end-start), 'seconds'