from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM
from tensorflow.python.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

#1) 데이터

datasets = load_boston()
x = datasets.data
y = datasets.target

# print(x.shape, y.shape)  # (506, 13) (506,)


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, shuffle = True, random_state = 66) 

# print(x_train.shape, x_test.shape)   # (354, 13) (152, 13)


scaler = RobustScaler() #scaler = MinMaxScaler() #scaler = StandardScaler() #scaler = MaxAbsScaler()

x_train = scaler.fit_transform(x_train).reshape(354,13,1)
x_test = scaler.transform(x_test).reshape(152,13,1)

#2) 모델링

model = Sequential()
model.add(LSTM(80, input_shape = (13,1))) 
model.add(Dense(45))
model.add(Dense(1))


#3. 컴파일, 훈련

model.compile(loss = 'mse', optimizer = 'adam') 

es = EarlyStopping(monitor='val_loss', patience=10, mode = 'auto', restore_best_weights=True)

model.fit(x_train, y_train, epochs = 1000, validation_split=0.2, callbacks=[es], batch_size = 50)


#4 평가예측
loss = model.evaluate(x_test,y_test)
print('loss: ', loss)

y_predict = model.predict(x_test)

r2 = r2_score(y_test, y_predict) 
print('r2스코어 : ', r2)

"""
-LSTM-
 loss:  16.40131950378418
r2스코어 :  0.8014779145049183   
  
-CNN-
loss :  7.7401814460754395
R2 :  0.906312596952948 

-DNN-
#loss :  23.494508743286133
#r2스코어 :  0.7216934825017536
"""


