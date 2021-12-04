from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.models import Sequential,Model,load_model
from tensorflow.keras.layers import Dense,Input
from tensorflow.keras.callbacks import EarlyStopping

datasets = load_iris()

x = datasets.data
y = datasets.target

#print(x.shape, y.shape)  # (150, 4) (150,)

from tensorflow.keras.utils import to_categorical
y = to_categorical(y)   #One Hot Encoding
print(y)
print(y.shape)   # (150, 3)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, shuffle=True, random_state=66)

scaler = MinMaxScaler()
#scaler = StandardScaler()
#scaler = RobustScaler()
#scaler = MaxAbsScaler()

scaler.fit(x_train)  # 어느 비율로 나눌지
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test) #x_train에 맞는 비율로 들어가있움





#2) 모델구성
'''
input1 = Input(shape=(4,))  
dense1 = Dense(10,activation = 'relu')(input1)  
dense2 = Dense(30, activation='relu')(dense1)   
dense3 = Dense(40)(dense2)
dense4 = Dense(50)(dense3)
output1 = Dense(3,activation = 'softmax')(dense4)
model = Model(inputs=input1, outputs=output1) 
'''
model = load_model("./_save/keras_04_iris_save_model.h5")

'''
model = Sequential()
model.add(Dense(10, activation = 'relu', input_dim = 4))     
model.add(Dense(30, activation = 'relu'))
model.add(Dense(40))
model.add(Dense(50))
model.add(Dense(3, activation = 'softmax'))
'''


#model.summary()

#3) 컴파일, 훈련
'''
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])  

es=EarlyStopping
es = EarlyStopping(monitor = 'val_loss', patience = 10, mode = 'min', verbose=1, restore_best_weights=True) 

model.fit(x_train,y_train,epochs=10000, batch_size=1, validation_split=0.2, callbacks=[es])
model.save("./_save/keras_04_iris_save_model.h5")
'''

#4) 평가, 예측


loss=model.evaluate(x_test, y_test)  
print('loss: ', loss[0]) 
print('accuracy: ', loss[1])
'''
results=model.predict(x_test[:7])
print(y_test[:7])  
print(results)
'''

#loss:  0.1277729719877243
# accuracy:  0.9333333373069763


"""
##################################### relu 적용 후 
# 그냥
loss:  0.08166332542896271
accuracy:  0.9666666388511658

# MinMAX
loss:  0.04720799997448921
accuracy:  1.0

#Standard
loss:  0.9328978061676025
accuracy:  0.8999999761581421

# robust 
loss:  0.2950940430164337
accuracy:  0.9333333373069763

# maxabs
loss:  0.07083969563245773
accuracy:  1.0
== relu함수를 앞쪽에 넣어주었다! standard와 robust의 경우에는 relu함수를 넣고나서 loss의 값이 더 나빠졌다!
나머지들은 good!

######################summary
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 10)                50
_________________________________________________________________
dense_1 (Dense)              (None, 30)                330
_________________________________________________________________
dense_2 (Dense)              (None, 40)                1240
_________________________________________________________________
dense_3 (Dense)              (None, 50)                2050
_________________________________________________________________
dense_4 (Dense)              (None, 3)                 153
=================================================================
Total params: 3,823
Trainable params: 3,823
Non-trainable params: 0

Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 4)]               0
_________________________________________________________________
dense (Dense)                (None, 10)                50
_________________________________________________________________
dense_1 (Dense)              (None, 30)                330
_________________________________________________________________
dense_2 (Dense)              (None, 40)                1240
_________________________________________________________________
dense_3 (Dense)              (None, 50)                2050
_________________________________________________________________
dense_4 (Dense)              (None, 3)                 153
=================================================================
Total params: 3,823
Trainable params: 3,823
Non-trainable params: 0


# MaxAbsScaler
loss:  0.09498904645442963
accuracy:  0.9666666388511658











"""