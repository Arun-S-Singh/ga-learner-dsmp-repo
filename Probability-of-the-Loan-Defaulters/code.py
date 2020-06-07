# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)


#Code starts here

### TASK 1
p_a = len(df[df['fico'] > 700])/len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = (len(df1[df1['fico'] > 700])/len(df))/p_b
result = (p_a_b == p_a)
print(result)

### TASK 2
prob_lp = len(df[df['credit.policy']=='Yes'])/len(df)
prob_cs = len(df[df['paid.back.loan']=='Yes'])/len(df)
new_df = df[df['paid.back.loan']=='Yes']
prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
bayes = (prob_pd_cs*prob_cs)/prob_lp
bayes = np.around(bayes,4)
print(bayes)

### TASK 3
df1 = df[df['paid.back.loan']=='No']
df1.groupby('purpose')['customer.id'].count().sort_values(ascending=False).plot(kind='bar')
plt.title('Distribution of Purpose for loans not paid back')
plt.show()
print(df1.shape)

### TASK 4
inst_median = df['installment'].median()
inst_mean =  df['installment'].mean()
df['installment'].hist()
plt.axvline(inst_median, color='k', linestyle='dashed', linewidth=1)
plt.axvline(inst_mean, color='r', linestyle='dashed', linewidth=1)
plt.xlabel('Installment')
plt.title('Frequency of Installment')
plt.show()

df['log.annual.inc'].hist()
plt.axvline(df['log.annual.inc'].median(), color='k', linestyle='dashed', linewidth=1)
plt.axvline(df['log.annual.inc'].mean(), color='r', linestyle='dashed', linewidth=1)
plt.xlabel('Log of Annual income')
plt.title('Frequency of Log of Annual income')
plt.show()



