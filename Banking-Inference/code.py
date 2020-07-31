# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency
import scipy

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)


#Code starts here

##Confidence Interval
data_sample = data.sample(n=sample_size,random_state=0)

true_mean = np.around(data['installment'].mean(),2)

sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()

error_margin = z_critical * (sample_std/math.sqrt(sample_size))

confidence_interval = np.around((sample_mean - error_margin),2) , np.around((sample_mean + error_margin),2)

in_confidence_interval = ((true_mean >= confidence_interval[0]) & (true_mean <= confidence_interval[1]))

print('z-critical = {0}'.format(z_critical))

print('True mean = {0}'.format(true_mean))

print('Sample size = {0}'.format(sample_size))
print('Sample mean = {0}'.format(sample_mean))
print('Sample std = {0}'.format(sample_std))

print('Margin of error = {0}'.format(error_margin))

print('{0} :: {1} :: {2}'.format(confidence_interval , true_mean ,in_confidence_interval))

## CLT
sample_sizes = [20,50,100]
sample_means = []

for sample_size in sample_sizes:
    print(sample_size)
    for i in range(1,1001,1):
        data_sample = data.sample(n=sample_size)
        sample_mean = data_sample['installment'].mean()
        sample_means.append(np.around(sample_mean,2))

    fig, ax = plt.subplots()
    plt.title('Sample Size = {0}'.format(sample_size), fontsize=15)
    plt.hist(sample_means,normed=True)
    plt.show()


## Small Business Interests
data['int.rate'] = data['int.rate'].str.rstrip('%').astype('float')
sbus = data[data['purpose']=='small_business']
#print(sbus.head())

value = data['int.rate'].mean()

int_population_std = sbus['int.rate'].std()
int_sample_size = sbus.shape[0]

#z_statistic_1, p_value_1 = ztest(x1=sbus['int.rate'],value=12,alternative='larger')
z_statistic_1, p_value_1 = ztest(x1=sbus['int.rate'],value=value,alternative='larger')

print('Small Business Sample Mean = {0}'.format(value))
print('Interest rate Population Deviation = {0} '.format(int_population_std))
print('Interest rate Sample Shape = {0} '.format(int_sample_size))

print('z_statistic_1 = {0}'.format(z_statistic_1))
print('p_value_1 = {0}'.format(p_value_1))

## Installment vs Loan Defaulting
x1 = data[data['paid.back.loan']=='No']['installment']
x2 = data[data['paid.back.loan']=='Yes']['installment']

z_statistic_2, p_value_2 = ztest(x1=x1,x2=x2,alternative='two-sided')

print('Count of not paid back loan = {0}'.format(x1.shape[0]))
print('Count of paid back loan = {0}'.format(x2.shape[0]))
print('z_statistic_2 = {0}'.format(z_statistic_2))
print('p_value_2 = {0}'.format(p_value_2))

## Purpose vs Loan Defaulting
observed = pd.crosstab(data['purpose'],data['paid.back.loan'],margins=False)

print(observed)

chi2, p, dof, ex = stats.chi2_contingency(observed)

print('Chi2 = {0} '.format(chi2))
print('Critical Value = {0}'.format(critical_value))

if chi2 > critical_value:
    print('REJECT Null Hypothesis : Distribution of purpose across all customers is same')
else:
    print('ACCEPT Null Hypothesis : Distribution of purpose across all customers is same')



