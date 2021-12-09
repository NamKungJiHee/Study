from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np
from tensorflow.keras.models import Sequential,Model,load_model
from tensorflow.keras.layers import Dense,Input,Dropout
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint

datasets = load_diabetes()
x = datasets.data
y = datasets.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.9, shuffle=True, random_state=66)   

scaler = MinMaxScaler()
#scaler = StandardScaler()
#scaler = RobustScaler()
#scaler = MaxAbsScaler()

scaler.fit(x_train) 
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test) 


#2) 모델구성

model = Sequential()
model.add(Dense(100,input_dim=10))
model.add(Dense(100))
model.add(Dense(100))
model.add(Dropout(0.1))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dropout(0.5))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation = 'relu'))



#model = load_model("./_save/keras_02_diabets_save_model.h5")

model.summary()

#3) 컴파일, 훈련

model.compile(loss='mse', optimizer='adam')

# #####################################################################################
# import datetime
# date = datetime.datetime.now()   #현재시간
# datetime = date.strftime("%m%d_%H%M")  #string형태로 만들어랏!  %m%d_%H%M = 월일/시/분    #1206_0456
# #print(datetime)

# filepath = './_ModelCheckPoint/'
# filename = '{epoch:04d}-{val_loss:.4f}.hdf5' #04d: 4자리까지(ex:9999),,, 4f: 소수 4제자리까지빼라     # hish에서 반환한 값이 epoch랑 val_loss로 들어가는것
# model_path = "".join([filepath, 'k27_' , datetime, '_', filename])  #" 구분자가 들어갑니다. ".join  <---

# #   ./_ModelCheckPoint/k26_1206_0456_2500-0.3724.hdf5

# ########################################################################################


es = EarlyStopping(monitor='val_loss', patience=10, mode='min',verbose=1, restore_best_weights=False)
mcp = ModelCheckpoint(monitor='val_loss', mode='auto',verbose=1, save_best_only=True, filepath = './_ModelCheckPoint/keras28_2_MCP.hdf5') 

model.fit(x_train, y_train, epochs=10000, batch_size=5, validation_split=0.11111111, callbacks=[es,mcp])
model.save("./_save/keras_028.2_diabets_save_model.h5")



#4) 평가, 예측

print("============================1. 기본 출력=======================")

loss= model.evaluate(x_test, y_test)
print('loss: ', loss)

y_predict = model.predict(x_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict) 
print('r2스코어 : ', r2)

print("============================2. load_model 출력=======================")

model2 = load_model('./_save/keras_028.2_diabets_save_model.h5')  

loss2= model2.evaluate(x_test, y_test)
print('loss2: ', loss2)

y_predict2 = model2.predict(x_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict2) 
print('r2스코어 : ', r2)


print("============================3. ModelCheckPoint 출력=======================")

model3 = load_model('./_ModelCheckPoint/keras28_2_MCP.hdf5')  

loss3= model3.evaluate(x_test, y_test)
print('loss3: ', loss3)

y_predict3 = model3.predict(x_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict3) 
print('r2스코어 : ', r2)


"""
loss:  3938.99267578125
r2스코어 :  0.5050695774953047
============================2. load_model 출력=======================
2/2 [==============================] - 0s 0s/step - loss: 3938.9927
loss2:  3938.99267578125
r2스코어 :  0.5050695774953047
============================3. ModelCheckPoint 출력=======================
2/2 [==============================] - 0s 997us/step - loss: 3691.8381
loss3:  3691.838134765625
r2스코어 :  0.536124250093914
  
  
 dropout 적용시 
  
============================1. 기본 출력=======================
2/2 [==============================] - 0s 996us/step - loss: 3345.3674
loss:  3345.367431640625
r2스코어 :  0.5796579864413991
============================2. load_model 출력=======================
2/2 [==============================] - 0s 997us/step - loss: 3345.3674
loss2:  3345.367431640625
r2스코어 :  0.5796579864413991
============================3. ModelCheckPoint 출력=======================
2/2 [==============================] - 0s 997us/step - loss: 3489.6111
loss3:  3489.611083984375
r2스코어 :  0.5615339111478113
  
  
  
"""