#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import math
import time


w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]  #14个优化参数
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print type(w[1])
alpha = 0.00005
fun = 0
epoch = 0
for ii in range(14):
    fun = fun + w[ii]*x[ii]
    print fun
while 1:
    epoch = epoch + 1
    # time.sleep(0.1)
    errs = math.fabs(fun-x[14])
    print "步数="+str(epoch),errs
    if  errs>0.001:
        for i in range(14):
            w[i] = w[i]-alpha*(fun-x[14])*x[i]
            print i , w[i]
            # time.sleep(0.01)
        fun = 0
        for j in range(14):
            fun = fun + w[j]*x[j]

    else:
        break
