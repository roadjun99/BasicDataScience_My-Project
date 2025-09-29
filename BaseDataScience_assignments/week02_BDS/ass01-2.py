import numpy as np
arr=np.arange(1,51)
print(arr%2==0)
total_even=(arr%2==0).sum()
print(total_even)
arr2=arr[arr%2==0]
print(arr2)