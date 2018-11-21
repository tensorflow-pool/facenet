# -*- coding: utf-8 -*-
import tensorflow as tf

tf.InteractiveSession()

q = tf.FIFOQueue(2, "float")
init = q.enqueue_many(([0, 0],))

x = q.dequeue()
y = x + 1
q_inc = q.enqueue([y])

init.run()
q_inc.run()
q_inc.run()
q_inc.run()
x.eval()  # 返回1
x.eval()  # 返回2
x.eval()  # 卡住
