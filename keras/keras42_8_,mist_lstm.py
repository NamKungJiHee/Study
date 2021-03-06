from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM
from tensorflow.python.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np 
from sklearn.model_selection import train_test_split
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

#1) 데이터

(x_train, y_train), (x_test, y_test) = mnist.load_data()
#print(x_train.shape, y_train.shape)    # (60000, 28, 28) (60000,)  
#print(x_test.shape, y_test.shape)      # (10000, 28, 28) (10000,)  


#print(np.unique(y_train, return_counts=True)) #  다중분류

y_train = to_categorical(y_train)   
#print(y_train.shape)   #(60000, 10)
y_test = to_categorical(y_test)
#print(y_test.shape)


# n = x_train.shape[0]
# x_train = x_train.reshape(n,-1)/255.       

# m = x_test.shape[0]
# x_test = x_test.reshape(m,-1)/255.

# print(x_train.shape, x_test.shape)

#2) 모델링

model = Sequential()
model.add(LSTM(80, input_shape = (28,28))) 
model.add(Dense(45))
model.add(Dense(10, activation ='softmax'))


#3. 컴파일, 훈련

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam',metrics=['accuracy']) 

es = EarlyStopping(monitor='val_loss', patience=50, mode = 'auto', restore_best_weights=True)

model.fit(x_train, y_train, epochs = 1000, validation_split=0.2, callbacks=[es], batch_size = 50)


#4 평가예측
loss = model.evaluate(x_test,y_test)


""" 
-LSTM-
loss: 0.2073 - accuracy: 0.9352
-CNN-
 loss:  [0.06073908135294914, 0.9817000031471252]
-DNN-
loss:  [0.24267248809337616, 0.9352999925613403]
"""

