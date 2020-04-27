# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.concatenate((data,new_record),axis=0)

age = census[:,0]

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.around(np.mean(age),2)
age_std = np.around(np.std(age),2)


race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

len_0 = np.size(race_0)
len_1 = np.size(race_1)
len_2 = np.size(race_2)
len_3 = np.size(race_3)
len_4 = np.size(race_4)

min_race = np.min([len_0,len_1,len_2,len_3,len_4])

if len_0 == min_race:
    minority_race = 0
elif  len_1 == min_race:
    minority_race = 1
elif  len_2 == min_race:
    minority_race = 2
elif  len_3 == min_race:
    minority_race = 3
elif len_4 == min_race:
    minority_race = 4


senior_citizens = census[census[:,0] > 60]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = np.size(senior_citizens,axis = 0)

avg_working_hours = np.around(working_hours_sum / senior_citizens_len ,2)

print(avg_working_hours)

high = census[census[:,1] > 10]
low =  census[census[:,1] <= 10]

avg_pay_high = np.around(np.mean(high[:,7]),2)
avg_pay_low = np.around(np.mean(low[:,7]),2)





