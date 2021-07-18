import pandas as pd

df = pd.read_csv('test_pandas/iris_sample.csv')
print(df)

#위에서 5줄만 읽을때(기본값 : 5, df.head(5))
print(df.head())

<<<<<<< HEAD
#iloc을 이용한 index이용방법
#원하는 행 만 뽑을때
print(df.iloc[[0,2],:])
print(df.iloc[[0,2]]) #생략가능

#원하는 열 만 뽑을때
print(df.iloc[:,[1,4]])

#loc을 이용한 이름이용 방법
print(df.loc[[0,2],:])
print(df.loc[:,['sepal_length','species']])
print(df[['sepal_length','species']]) #축양형(loc없음)

#원하는 값 출력
print(df.loc[2:3, 'petal_length': 'species'])
=======
#원하는 행만 뽑을 때(열은 반대)
print(df.iloc[[0,2],:])
print(df.iloc[[0,2]])#축약형

#loc을 이용한 뽑는 법(인덱스 이름으로)
print(df.loc[[0,2],['sepal_length','sepal_width']])
print(df.loc[0:2,'sepal_length':'sepal_width'])

#열을 선택하는 축약형
print(df[['sepal_length','sepal_width']])
>>>>>>> fa2bb23204c98d067f144e68bc900da8d6039c7a
