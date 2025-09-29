# DataFrame의 행 인덱스를 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'로 설정
# Product 변수(열)의 값이 A, B, ... J 이므로 이 값을 이용
import pandas as pd
import numpy as np
# DataFrame 객체의 사본 생성
df = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Price': [100, 200, 150, 300, 250, 130, 120, 180, 220, 270],
    'Quantity': [10, 5, 8, 6, 9, 15, 12, 7, 10, 8],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Electronics',
                 'Clothing', 'Electronics', 'Clothing', 'Electronics',
                 'Clothing', 'Clothing']
}
df_2=pd.DataFrame(df.copy())
print(df_2.index)
# df_new 객체의 행 인덱스를 Product 변수의 값으로 설정
# 변수 이름이 함께 추출되지 않도록 pandas.DataFrame.to_numpy 함수 활용
df_2.index=df_2['Product'].to_numpy()
# DataFrame 출력
print(df_2)
df_2.index.name=None
print(df_2)
# 2-2
d = ['Laptop', 'Jacket', 'Smartphone', 'Headphones', 'Sweater', \
     'Tablet', 'Scarf', 'Camera', 'Jeans', 'Hat']
arr1=np.array(d)
df_2['Product']=arr1
print(df_2)
# 2-3
df_2=pd.DataFrame(df_2,columns=['Product','Category','Price','Quantity'])
print(df_2)
# 2-4
print(df_2.describe())
# 2-5
df_2['P*Q']=df_2['Price']*df_2['Quantity']
print(df_2)