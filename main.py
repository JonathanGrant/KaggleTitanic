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

prediction_writer.writerow(['PassengerID','Survived'])
for row in test_file:
    if row[3] == 'female':
        prediction_writer.writerow([row[0],'1'])
    else:
        prediction_writer.writerow([row[0],'0'])
prediction_file.close()

end = time.time()
print 'Total time elpased:', (end-start), 'seconds'