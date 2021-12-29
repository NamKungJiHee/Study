from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout,Conv2D,Flatten
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#1. 데이터
train_datagen = ImageDataGenerator(
    rescale=1./255, 
    horizontal_flip = True,  
    vertical_flip = True,
    width_shift_range= 0.1,
    height_shift_range= 0.1,
    rotation_range= 5,
    zoom_range = 1.2,
    shear_range = 0.7,
    fill_mode= 'nearest')   
 
test_datagen = ImageDataGenerator(rescale=1./255) 

xy_train = train_datagen.flow_from_directory(
    '../_data/image/catdog/cat_dog/training_set/training_set/', 
    target_size = (100,100), 
    batch_size=8100,
    class_mode = 'binary',
    shuffle= True) 
# Found 8005 images belonging to 2 classes.

xy_test = test_datagen.flow_from_directory(
    '../_data/image/catdog/cat_dog/test_set/test_set/',
    target_size = (100,100),
    batch_size = 11000,
    class_mode = 'binary') 
# Found  10028 images belonging to 2 classes.

x_train = xy_train[0][0]
y_train = xy_train[0][1]
x_test = xy_test[0][0] 
y_test = xy_test[0][1]
# print(x_train.shape, y_train.shape) # (8005, 100, 100, 3) (8005,)
# print(x_test.shape, y_test.shape) # (2023, 100, 100, 3) (2023,)

augment_size = 2000
randidx = np.random.randint(x_train.shape[0], size = augment_size)

# print(x_train.shape[0])  # 8005
# print(randidx) # [4718 1326 5431 ... 2839 2663 3981]
# print(np.min(randidx), np.max(randidx)) # 0 8000

x_augmented = x_train[randidx].copy()  #copy() 메모리 생성
y_augmented = y_train[randidx].copy()  
# print(x_augmented.shape) # (2000, 100, 100, 3)
# print(y_augmented.shape) # (2000,)

x_augmented = x_augmented.reshape(x_augmented.shape[0], x_augmented.shape[1], x_augmented.shape[2], 3)
x_train = x_train.reshape(x_train.shape[0],x_train.shape[1],x_train.shape[2],3)
x_test = x_test.reshape(x_test.shape[0],x_test.shape[1],x_test.shape[2],3)

x_augmented = train_datagen.flow(x_augmented, y_augmented,   #np.zeros(augument_size), 
                                  batch_size= augment_size, shuffle= False).next()[0] #save_to_dir='../_temp/').next()[0]  # 증폭

#print(x_augmented)
#print(x_augmented.shape)  # (2000, 100, 100, 3)

# concatenate, merge 합치기 위한 것!

x_train = np.concatenate((x_train, x_augmented))  
y_train = np.concatenate((y_train, y_augmented))  
# print(x_train.shape, y_train.shape)  # (10005, 100, 100, 3) (10005,)
# print(np.unique(y_train)) # [0. 1.]

#2. 모델
model = Sequential()
model.add(Conv2D(128, (2,2), input_shape= (100,100,3), activation= 'relu'))
model.add(Conv2D(64, (2,2), padding='same'))  
model.add(Conv2D(16, (2,2)))
model.add(Flatten())
model.add(Dense(256))
model.add(Dropout(0.5))
model.add(Dense(1, activation = 'sigmoid'))

#3. 컴파일, 훈련
model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics = ['acc'])

es = EarlyStopping(monitor='val_loss', patience=20, mode = 'auto', restore_best_weights=True)

model.fit(x_train, y_train, epochs=70, batch_size=20, validation_split=0.2, callbacks=[es]) 

#4)평가, 예측
loss= model.evaluate(x_test, y_test)
print('loss: ', loss)    

''' 
loss:  [0.7593091130256653, 0.5318833589553833]
'''