# -*- coding: utf-8 -*-
from tushare2 import handGun
from tushare2 import carbine
class gunFactory():
    def __init__(self,gun_type):
        self.gun_type = gun_type
    def produce(self):
        if handGun == self.gun_type:
            return handGun()
        else:
            return carbine()


fa = gunFactory(handGun)
gun = fa.produce()
gun.fire()

fa = gunFactory(carbine)
gun = fa.produce()
gun.fire()



#########实例属性
class test():
    def __init__(self):
       self._name='Amy'
       self._age=10
    def printinfo(self):
       print self._name,self._age
###########################################################第一种方法
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value

    name = property(fget=get_name,fset=set_name)
###########################################################第二种方法
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value
#############################################################
someone = test()
someone.printinfo()

someone.set_name("alice")

print someone.name
someone.name = 'Alice'
print someone.name

print someone.age
someone.age = 100
print someone.age



################虚函数性质，同名覆盖
class father():
    def pri(self):
        print 'father'
    def ppp(self,cads):
        print cads

class pri(father):
    def pri(self):
        print 'son'

class son2(father):
    pass

class walker():
    def pri(self,fat):
        fat.pri()

a = father()
a.pri()
a.ppp('fdfd')
print '11111'
b = pri()
b.pri()
print '22222'
c=son2()
c.pri()
print '3333'
x = walker()
x.pri(a)
x.pri(b)
x.pri(c)