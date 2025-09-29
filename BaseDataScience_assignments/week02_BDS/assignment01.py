import numpy as np
arr = np.array([[10, 15, 30, 40],
                [50, 60, 70, 80],
                [90, 95, 85, 75],
                [65, 55, 45, 35]])
indexMax=np.argmax(arr)
indexMin=np.argmin(arr)
unraveled_index=np.unravel_index(np.argmax(arr),(4,4))
unindex_2=np.unravel_index(np.argmin(arr),(4,4))
print(f"최대값 인덱스: %d"%indexMax)
print(f"4x4 배열에서의 최댓값 위치: {unraveled_index}")
print("최소값 인덱스: %d"%indexMin)
print(f"4x4 배열에서의 최솟값 위치: {unindex_2}")