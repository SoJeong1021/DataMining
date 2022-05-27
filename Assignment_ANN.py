import tensorflow
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam 
import numpy as np

num_classes = 10

img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 28*28).astype('float32')
x_test  = x_test.reshape(-1, 28*28).astype('float')

x_train = x_train / 255
x_test  = x_test / 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes)
y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(512, input_shape=(28*28,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(),
    metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=5, batch_size=32)

print(history.history['loss'])
print(history.history['accuracy'])

y_predict = model.predict(x_test)

scores = model.evaluate(x_test, y_test, batch_size=32)

print('Test loss=', scores[0])
print('Test accuracy=', scores[1])