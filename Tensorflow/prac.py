# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:30:02 2018

@author: M61958
"""

import tensorflow as tf 

x = tf.placeholder(tf.int32 , name ='x' , shape= [3])
y= tf.placeholder(tf.int32 , shape=[3] , name ='y')

sum_x = tf.reduce_sum(x,name = 'sum_x')
product_x = tf.reduce_prod(y, name='prod_y')

final_div = tf.div(sum_x,product_x,name = 'final_div')

with tf.Session() as sess:
    print ('The sum of x is ' , sess.run(sum_x , feed_dict = { x:[100,200,300] }))
    print ('The product of y is ' , sess.run(product_x , feed_dict = { y:[11,22,33] }))
    
    print ('The division is ' , sess.run(final_div , feed_dict = { x:[100,200,300] , y:[1,2,3] } ))
    
    writer = tf.summary.FileWriter('./SimpleMathPlaceholders' , sess.graph)
    writer.close()