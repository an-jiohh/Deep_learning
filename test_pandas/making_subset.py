import pandas as pd

df = pd.read_csv('test_pandas/iris_sample.csv')
print(df)

#위에서 5줄만 읽을때(기본값 : 5, df.head(5))
print(df.head())