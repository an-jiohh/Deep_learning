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
df2_read = pd.read_csv('tmp.csv')
print(df2_read)

#원하지 않은 col이 들어온경우 
#index colum이 인식되서 이런 현상이 발생
#방법 1. index열을 지정(index_col)
df3 = pd.read_csv('tmp.csv', index_col=0)
print(df3)
#방법 2. 특정열을 제거
df2_read = pd.read_csv('tmp.csv')
#확인하기 위해 해더 출력
print(df2_read.columns)
#'unnamed: 0'헤더 삭제
df2_read.drop(['Unnamed: 0'],axis=1)
print(df2_read) #제거를하고 재선언을 해줘야함
df4_read = df2_read.drop(['Unnamed: 0'],axis=1)
print(df4_read)
# 추가적으로 행(index = 0)을 제거하려면?(drop)
df4_read = df4_read.drop(index=0)
print(df4_read)