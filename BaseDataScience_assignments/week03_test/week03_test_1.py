import pandas as pd
import numpy as np
from pandas import Series, DataFrame

obj=pd.Series([4,7,-5,3],index=['d','b','a','c'])
data= {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame=pd.DataFrame(data)
frame2=pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four',
                             'five', 'six'])

df_raw = pd.DataFrame({'var1': [1,2,1],
                       'var2': [2,3,2]})
df=pd.DataFrame({'var1': [4,3,8],
                  'var2': [2,6,1]})
df['var_sum'] = df['var1'] + df['var2']
df['var_mean'] = (df['var1'] + df['var2']) / 2

print(df)