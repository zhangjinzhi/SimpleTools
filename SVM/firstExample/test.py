# -*- coding:utf-8 -*-
import os
os.chdir('C:\libsvm-3.21\python')#请根据实际路径修改
from svmutil import *


y, x = svm_read_problem('../heart_scale')#读取自带数据

m = svm_train(y[:200], x[:200], '-c 4')

p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)

print 

y, x = svm_read_problem('train1.txt')#读入训练数据
yt, xt = svm_read_problem('test1.txt')#训练测试数据
m = svm_train(y, x )#训练
svm_predict(yt,xt,m)#测试

print

y, x = svm_read_problem('371.txt')#读入训练数据
yt, xt = svm_read_problem('245.txt')#训练测试数据
m = svm_train(y, x )#训练
svm_predict(yt,xt,m)#测试