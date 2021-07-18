import sklearn
import pandas as pd

print(sklearn.__version__)

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

iris_data = iris.data
iris_label = iris.target
print('iris target value:', iris_label)
print('iris target name:', iris.target_names)

df_iris = pd.DataFrame(data=iris_data,columns=iris.feature_names)
df_iris['label'] = iris.target
print(df_iris)

x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_label,test_size=0.2,random_state=11)

df_clf = DecisionTreeClassifier(random_state=11)
df_clf.fit(x_train,y_train)