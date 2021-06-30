from tensorflow import keras
import numpy as np

x = np.array([0,1,2,3,4], dtype='float64')
y = 2*x+1
print(y)

model = keras.models.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
model.compile('SGD', 'mse')
model.fit(x, y, epochs=1000)

print(model.predict([0,10,7,3,1,1.9]))