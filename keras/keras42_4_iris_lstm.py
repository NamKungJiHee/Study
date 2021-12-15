from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM
from tensorflow.python.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris 

#1) 데이터
datasets = load_iris()

x = datasets.data
y = datasets.target

#print(x.shape, y.shape)  # (150, 4) (150,)

from tensorflow.keras.utils import to_categorical
y = to_categorical(y)  
#print(y)
#print(y.shape)   # (150, 3)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, shuffle = True, random_state = 66) 

#print(x_train.shape,x_test.shape)  # (105, 4) (45, 4)

scaler = RobustScaler() #scaler = MinMaxScaler() #scaler = StandardScaler() #scaler = MaxAbsScaler()

x_train = scaler.fit_transform(x_train).reshape(105,4,1)
x_test = scaler.transform(x_test).reshape(45,4,1)


#2) 모델링

model = Sequential()
model.add(LSTM(80, input_shape = (4,1))) 
model.add(Dense(45))
model.add(Dense(3, activation ='softmax'))


#3. 컴파일, 훈련

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam',metrics=['accuracy']) 

es = EarlyStopping(monitor='val_loss', patience=50, mode = 'auto', restore_best_weights=True)

model.fit(x_train, y_train, epochs = 1000, validation_split=0.2, callbacks=[es], batch_size = 50)


#4 평가예측
loss = model.evaluate(x_test,y_test)

""" 
-LSTM-
loss: 0.1991 - accuracy: 0.9111
-CNN-
loss :  [0.039754826575517654, 0.9333333373069763]
-DNN-
loss:  [0.14235804975032806, 0.9333333373069763]
"""