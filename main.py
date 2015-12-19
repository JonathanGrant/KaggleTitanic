#https://www.kaggle.com/c/titanic/details/getting-started-with-python
import csv as csv
import numpy as np

file = csv.reader(open('train.csv','rb'))
header = file.next()
data = []
for row in file:
    data.append(row)
data = np.array(data)

num_passengers = np.size(data[0::,1].astype(np.float))
num_survivors = np.sum(data[0::,1].astype(np.float))
percent_survivors = num_survivors / num_passengers

women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"

women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

percent_women_survivors = np.sum(women_onboard) / np.size(women_onboard)
percent_men_survivors = np.sum(men_onboard) / np.size(men_onboard)

#Now open test file
test_file = csv.reader(open('test.csv','rb'))
header = test_file.next()

#Write to new file
prediction_file = open('genderbasedmodel.csv','wb')
prediction_writer = csv.writer(prediction_file)
