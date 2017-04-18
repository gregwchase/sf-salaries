import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salaries = pd.read_csv("/Users/gregorychase/Desktop/sf-salaries/Salaries.csv")

salaries.head()
# salaries.dtypes


# Convert object values to numeric
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

salaries.BasePay.mean()
salaries.OvertimePay.mean()
salaries.OtherPay.mean()
salaries.TotalPay.mean()

salaries.BasePay.median()
salaries.OvertimePay.median()
salaries.OtherPay.median()
salaries.TotalPay.median()

# Percent of data listed as full time (FT) or part time (PT)
pct_FT_or_PT = round(sum(salaries.Status.value_counts())/float(len(salaries)) * 100,2)

# Subset data based on Full Time (FT), Part Time (PT), or NaN
salaries_FT = salaries.loc[salaries['Status'] == 'FT']
salaries_PT = salaries.loc[salaries['Status'] == 'PT']
salaries_NaN = salaries[(salaries['Status']!='FT') & (salaries['Status']!='PT')]

# Convert most columns using convert_objects
# df = df.convert_objects(convert_numeric=True)

plt.scatter(salaries.Year, salaries.BasePay)
plt.show()
