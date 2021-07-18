import pandas as pd

#csv파일 가져오기
df = pd.read_csv("test_pandas/iris_sample.csv")
print(df.head())

#데이터 차원 구하기
print(df.shape)

#데이터 타입 구하기(열마다)
print(df.dtypes)

# 범주형 열(species)의 level별 분포를봅시다.
# 연속형 열은 의미 없습니다.
print(df['species'].value_counts())

"""# 그럼 연속형 열은? -> 히스토그램으로 봅니다.
# import matplotlib.pyplot as plt
# df[df.columns[0:4]].hist()
df.hist()
# bin 구간을 설정할 수도 있습니다.
df[df.columns[0:4]].hist()
# 그림을 본김에 연속형 변수의 산점도도 확인 할 수 있겠네요
# x축을 'sepal_length' y축을 'petal_length'로 보겠습니다.
df.plot.scatter(x='sepal_length', y='petal_length')
# 참고. matplotlib으로 plot그리기.
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(30)
print(data)

plt.figure(figsize=(10, 2))
plt.subplot(1, 2, 1)
plt.plot(data, '-')
plt.subplot(1, 2, 2)
plt.hist(data)
# 연속형 col의 summary statistics 출력해 봅시다.(통계적인 수치)
df.describe()
# 범주형 까지 보고싶다면요?
df.describe(include='all')
# 연속형 col의 box plot을 그려봅시다.
df.plot.box()
# 그밖에도 다양한 기초 통계와 관련된 함수가 마련되어 있습니다.
# sum, count, median, mean, var, std, max, min
df.mean()"""