#!/usr/bin/python

import pickle
import sys
# import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
salaries = []
bonuses = []
for point in data:
    salary = point[0]
    bonus = point[1]
    # matplotlib.pyplot.scatter( salary, bonus )
    salaries.append(salary)
    bonuses.append(bonus)

maxSalary = max(salaries)
maxBonus = max(bonuses)

maxSalaryIndex = salaries.index(maxSalary)
maxBonusIndex = bonuses.index(maxBonus)

print "When salary is maximum, index: ", maxSalaryIndex, "salary: ", salaries[maxSalaryIndex], "bonus: ", bonuses[maxSalaryIndex]
print "When bonus is maximum, index: ", maxBonusIndex, "salary: ", salaries[maxBonusIndex], "bonus: ", bonuses[maxBonusIndex]

for key in data_dict.keys():

    sal = data_dict[key]["salary"]
    bon = data_dict[key]["bonus"]
    if sal == maxSalary:
        print "Salary outlier: ", key
        # data_dict.pop(key, 0)
    if bon > 5000000 and bon != "NaN" and sal > 1000000:
        print "Bonus outlier: ", key, "and bonus: ", bon

# print "Data: ", data_dict.keys()

"""matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()"""


