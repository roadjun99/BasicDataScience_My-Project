import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

# 주어진 데이터를 이용하여 데이터 프레임 객체를 생성하고 출력
scores_data = {
    'korean': [87, 70, 95, 85, 100, 78, 82],
    'english': [90, 85, 87, 88, 76, 91, 84],
    'math': [85, 79, 92, 86, 89, 95, 87],
    'science': [88, 79, 85, 86, 95, 100, 92],
    'history': [92, 81, 87, 90, 91, 89, 94],
    'CSE': [95, 89, 94, 90, 100, 93, 88],
    'AI': [87, 78, 88, 92, 85, 99, 95]
}
df_scores = pd.DataFrame(scores_data, index=['Alice', 'Bob', 'Charlie', 'David', 'Mike', 'Emma', 'Sophia'])
print("원본 데이터:")
print(df_scores)
#3-1
scr_d2=df_scores.copy()
scr_d2=pd.DataFrame(scr_d2)
scr_d2['total']=np.array(df_scores.sum(1))
scr_d2['average']=np.array(df_scores.mean(1))
print(scr_d2)
#3-2
print(scr_d2.describe())
print(scr_d2.info())
#3-3
scr_d2_HighAver=scr_d2[scr_d2['average']>=90]
print("평균 점수 90점 이상인 학생:")
print(scr_d2_HighAver)
#3-4
imin=scr_d2['average'].idxmin()
print(scr_d2.loc[[imin]])
imin2=scr_d2['average'].argmin()
print(scr_d2.iloc[[imin2]])
miner=scr_d2['average'].min()
print(scr_d2[scr_d2['average']==miner])