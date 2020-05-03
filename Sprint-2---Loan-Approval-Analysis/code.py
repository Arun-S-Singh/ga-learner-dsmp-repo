# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

########## STEP 1 ##########

#bank_data.info()
#bank_data.describe()

# Check all categorical values.
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var)

# Check all categorical values.
numerical_var = bank_data.select_dtypes(include= 'number')
print(numerical_var)

########## STEP 2 ##########

# Create new dataframe banks
banks = bank_data.drop('Loan_ID',axis=1)

print(banks.isnull().sum())

bank_mode = banks.mode()
#print(type(bank_mode))

banks.fillna(bank_mode,inplace=True)

for x in banks.columns.values:
    # df[x]=df[x].fillna(value=df_mode[x].iloc[0])
    banks[x] = banks[x].fillna(value=bank_mode[x].iloc[0])

print(banks.isnull().sum().values.sum())
print(banks.shape)

########## STEP 3 ##########

#avg_loan_amount = banks.groupby(['Gender', 'Married', 'Self_Employed']).agg({'LoanAmount':'mean'})
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')

print(avg_loan_amount['LoanAmount'][1])

########## STEP 4 ##########
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].shape[0]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].shape[0]

percentage_se = np.around((loan_approved_se / 614) * 100 , 2)
percentage_nse = np.around((loan_approved_nse / 614) * 100 , 2)

print(percentage_se)
print(percentage_nse)

########## STEP 5 ##########
banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].apply(lambda x : x / 12)

big_loan_term = banks[ banks['Loan_Amount_Term'] >= 25].shape[0]

print(big_loan_term)

########## STEP 6 ##########
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()

print(mean_values.iloc[1,0])




