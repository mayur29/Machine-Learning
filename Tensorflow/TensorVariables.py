# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:31:53 2018

@author: M61958
"""

import tensorflow as tf 

x = tf.placeholder(tf.float32,name ='x')
W = tf.Variable([2.5,4.0],tf.float32, name='var_W')
b = tf.Variable([5.0,10.0] ,tf.float32, name='var_b')

y = W*x+b

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print (  'y =' ,sess.run(y,feed_dict = {x:[ 10,100] }))
    
    
    
init = tf.initialize_variables([W])
with tf.Session() as sess:
    sess.run(init)
    print (  'y =' ,sess.run(y,feed_dict = {x:[ 10,100] }))