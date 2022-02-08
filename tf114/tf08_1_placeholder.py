# y = wx + b
import tensorflow as tf
tf.set_random_seed(77)  

#1. 데이터   
# x_train = [1,2,3]
# y_train = [1,2,3]
x_train = tf.placeholder(tf.float32, shape = [None])  ####### shape를 무조건 명시해줘야 한다. #######
y_train = tf.placeholder(tf.float32, shape = [None])  ####### shape를 무조건 명시해줘야 한다. #######

# w = tf.Variable(1, dtype = tf.float32) 
# b = tf.Variable(1, dtype = tf.float32) 
w = tf.Variable(tf.random_normal([1], dtype = tf.float32))
b = tf.Variable(tf.random_normal([1], dtype = tf.float32))

#2. 모델구성
hypothesis = x_train * w + b # y = wx + b  

#3-1. 컴파일
loss = tf.reduce_mean(tf.square(hypothesis - y_train))  
                                                        
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) 
train = optimizer.minimize(loss)  

#3-2. 훈련
sess = tf.compat.v1.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    #sess.run(train) 
    _, loss_val, W_val, b_val = sess.run([train, loss, w, b], feed_dict = {x_train:[1,2,3], y_train:[1,2,3]})   # train는 반환값이 없으므로 _, 라고 쓴다.
    if step % 20 == 0:
        #print(step, sess.run(loss), sess.run(w), sess.run(b)) 
        print(step, loss_val, W_val, b_val)
        
sess.close()     