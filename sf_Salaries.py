import numpy as np
import pandas as pd

salaries = pd.read_csv("/Users/gregorychase/Desktop/sf-salaries/Salaries.csv")


dims = salaries.shape

# Replace values marked "Not Provided"
# salaries = salaries.replace("Not Provided", np.NaN)
# salaries = salaries.replace(np.NaN,0)

# TotalComp already given as TotalPay, TotalPayBenefits
# salaries["TotalComp"] = salaries["BasePay"] + salaries["OvertimePay"] + salaries["OtherPay"]


# salaries.BasePay = salaries.BasePay.astype(np.int64)


# salaries = salaries.fillna({
#     'JobTitle': 'missing',
#     'BasePay': '0',
#     'OvertimePay': '0',
#     'OtherPay': '0',
#     'Benefits': '0',
#     'Year': '0',
#     'Status': '0'
# })

salaries.head()


salaries.dtypes


# Convert object values to numeric
# df = df.convert_objects(convert_numeric=True)
# 'coerce' converts invalid values to NaN, 'ignore' returns original Series
salaries['BasePay'] = pd.to_numeric(salaries['BasePay'], errors='coerce')
salaries['OvertimePay'] = pd.to_numeric(salaries['OvertimePay'], errors='coerce')
salaries['OtherPay'] = pd.to_numeric(salaries['OtherPay'], errors='coerce')

# Check values, then delete constant columns.
# 'inplace' changes the actual values.
# salaries.Agency.value_counts()
salaries.drop('Agency', axis=1, inplace=True)

# salaries.Notes.value_counts()
salaries.drop('Notes', axis=1, inplace=True)

# Fill all missing values/ NaN with 0
# df.fillna(0)


# Calculations of mean default to exclude NaN values
# Read in data
# Keep NaN data
# Convert columns to numeric
# Begin asking visualization questions

salaries.BasePay.mean()
salaries.OvertimePay.mean()
salaries.OtherPay.mean()

salaries.BasePay.median()
salaries.OvertimePay.median()
salaries.OtherPay.median()


# Percent of data listed as full time (FT) or part time (PT)
round(sum(salaries.Status.value_counts())/float(len(salaries)) * 100,2)

# Subset data based on full time and part time.
# Look at average salaries over time?
# Unsupervised learning - new categories based on JobTitle
# Toss any values out < 0?

# Convert most columns using convert_objects
# df = df.convert_objects(convert_numeric=True)
