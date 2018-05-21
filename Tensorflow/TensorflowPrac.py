# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:54:55 2018

@author: M61958
"""

import tensorflow as tf 

 a = tf.constant(6.5 , name ='constant_a')
 b = tf.constant(3.4 , name ='constant_b')
 c = tf.constant(3.0 , name= 'constant_c')
 d = tf.constant(100.2 , name= 'constant_d')
 
 add = tf.add(a,b,name='add_ab') 
 subtract = tf.subtract(b,c,name ='sub_bc')
 square = tf.square(d , name ='sqaure_d')
 
 final_sum = tf.add_n([add,subtract,square] , name= 'final_sum')
 
 with tf.Session() as sess :
     print("a +b" , sess.run(add))
     print ("b-c: " , sess.run(subtract))
     print ("sqaure: " , sess.run(square))
     
     anothersum = tf.add_n ([a,b,c,d,square] , name ="another_sum")
     print ("Another Sum " , sess.run(anothersum))
     
     
 writer = tf.summary.FileWriter('./SimpleMath' , sess.graph)
 writer.close()
 

