import pandas as pd

#csv파일 가져오기
df = pd.read_csv("test_pandas/iris_sample.csv")

#missing 값 확인
print(df.isna())

#각 컬럼별 missing 갯수 확인
print(df.isna().sum())

#missing이 있는 행을 버림
print(df.dropna())

#missing 확인
print(len(df),len(df.dropna()))