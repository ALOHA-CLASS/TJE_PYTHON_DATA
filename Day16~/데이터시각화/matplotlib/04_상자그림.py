import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


# 데이터
np.random.seed(5)
data = np.random.normal(loc=0, scale=1, size=100)

# 그래프 설정
# notch     : 노치(파여진 홈) 여부
# sym       : 특이점 표시 기호 
# showmeans : 평균 표시 여부
plt.boxplot(data, notch=True, sym='+', showmeans=True)

# 제목 및 라벨
plt.title('상자그림 데이터')
plt.xlabel('데이터')
plt.ylabel('값')

# 그래프 이미지 저장
plt.savefig('상자그림.png', dpi=400)

# 그래프 출력
plt.show()