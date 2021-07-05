import pandas as pd

df = pd.read_csv('test_pandas/iris_sample.csv')
print(df)

#위에서 5줄만 읽을때(기본값 : 5, df.head(5))
print(df.head())

#원하는 행만 뽑을 때(열은 반대)
print(df.iloc[[0,2],:])
print(df.iloc[[0,2]])#축약형

#loc을 이용한 뽑는 법(인덱스 이름으로)
print(df.loc[[0,2],['sepal_length','sepal_width']])
print(df.loc[0:2,'sepal_length':'sepal_width'])

#열을 선택하는 축약형
print(df[['sepal_length','sepal_width']])