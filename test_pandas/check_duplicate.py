import pandas as pd

#csv파일 가져오기
df = pd.read_csv("test_pandas/iris_sample.csv")
print(df)

print(df.duplicated()) #중복값 여부 출력
print(df.duplicated().sum()) #중복값 갯수 합쳐서 출력
print(df[df.duplicated()]) #중복되어있는 배열출력
print(df[df.duplicated(keep=False)]) #중복되어있는 배열출력(중복되있는거 모두)

#0~4까지 중복된 행들을 출력
print(df[df.duplicated(subset=df.columns[0:4])])

#중복된 값 버림
print(df.drop_duplicates())