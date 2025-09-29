import numpy as np
arr1=np.arange(2,31,2)
print(arr1)
arr2=arr1.reshape(3,5)
print(arr2)
Max=arr1.max()
Min=arr1.min()
arr3=(arr2-Min)/(Max-Min)
print(arr3)