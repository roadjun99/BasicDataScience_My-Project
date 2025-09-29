import numpy as np
arr1=np.random.randn(10000)
mean=arr1.mean()
std=arr1.std()
print(f"배열의 평균: {mean}")
print(f"배열의 표준편차: {std}")