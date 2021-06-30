import pandas as pd

#dic을 이용한 dataframe생성
df1 = pd.DataFrame({'a':[1,2,3],'de':[4,5,6]})
print(df1)

#list를 이용한 dataframe생성
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df2)

# df1과 똑같이 만들기 위해 header변경
df2.columns=['a','b','c']
print(df2)

# 결과파일 생성
df2.to_csv("tmp.csv")

# 결과파일 읽기
df2.to_csv("tmp2.csv", )
df2_read = pd.read_csv('tmp.csv')
print(df2_read)