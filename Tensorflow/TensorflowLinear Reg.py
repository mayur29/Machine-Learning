# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:11:46 2018

@author: M61958
"""

import tensorflow as tf 


#Variables 
W = tf.Variable([.3],dtype=tf.float32)
b = tf.Variable([-.3],dtype=tf.float32)


x= tf.placeholder(dtype=tf.float32 , name ='x')

# W is slope and b is y intercept 

linear_model= W*x+b

y = tf.placeholder(dtype= tf.float32 , name ='y')

loss = tf.reduce_sum(tf.square(linear_model-y))

optimizer = tf.train.GradientDescentOptimizer(0.01)

train = optimizer.minimize(loss)

x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train , {x:x_train , y:y_train})
    curr_w,curr_b,curr_loss = sess.run([W,b,loss] , {x:x_train , y:y_train})   
    print ("W : %s b: %s loss : %s" %(curr_w , curr_b , curr_loss ))

