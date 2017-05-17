# -*- coding: utf-8 -*-
#一个简单的pattern实例

import re
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print "p.pattern:", p.pattern
print "p.flags:", p.flags
print "p.groups:", p.groups
print "p.groupindex:", p.groupindex

### output ###
# p.pattern: (\w+) (\w+)(?P<sign>.*)
# p.flags: 16
# p.groups: 3
# p.groupindex: {'sign': 3}


#注：此处全局的变量名，写成name，只是为了演示而用
#实际上，好的编程风格，应该写成gName之类的名字，以表示该变量是Global的变量
name = "whole global name"

class Person:
    def __init__(self, newPersionName):
        #self.name = newPersionName;

        #1.如果此处不写成self.name
        #那么此处的name，只是__init__函数中的局部临时变量name而已
        #和全局中的name，没有半毛钱关系
        self.name = newPersionName;   #  self.name = newPersionName; 才是正确的！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                                      ## name = newPersionName; 是错误的
        #此处只是为了代码演示，而使用了局部变量name，
        #不过需要注意的是，此处很明显，由于接下来的代码也没有利用到此处的局部变量name
        #则就导致了，此处的name变量，实际上被浪费了，根本没有利用到

    def sayYourName(self):
        #此处由于找不到实例中的name变量，所以会报错：
        #AttributeError: Person instance has no attribute 'name'
        print 'My name is %s'%(self.name);

def selfAndInitDemo():
    persionInstance = Person("crifan");
    persionInstance.sayYourName();

###############################################################################
if __name__=="__main__":
    selfAndInitDemo();

################################################################
########################################################################################上下变量的作用域对比
#######################################################################################上下变量的作用域对比
######################################################################################上下变量的作用域对比
#####################################################################################上下变量的作用域对比
print ''
#注：此处全局的变量名，写成name，只是为了演示而用
#实际上，好的编程风格，应该写成gName之类的名字，以表示该变量是Global的变量
name = "whole global name";

class Person:
    name = "class global name"
    print '11111111 name=%s'%(name)
    def __init__(self, newPersionName):
        #self.name = newPersionName;

        #此处，没有使用self.name
        #而使得此处的name，实际上仍是局部变量name
        #虽然此处赋值了，但是后面没有被利用到，属于被浪费了的局部变量name
        print '类的参数传入后，自动赋值为newPersonalName'
        name = newPersionName;
        print 'local value name=%s'%(name)

    def sayYourName(self):
        #此处，之所以没有像之前一样出现：
        #AttributeError: Person instance has no attribute 'name'
        #那是因为，虽然当前的实例self中，没有在__init__中初始化对应的name变量，实例self中没有对应的name变量
        #但是由于实例所对应的类Person，有对应的name变量,所以也是可以正常执行代码的
        #对应的，此处的self.name，实际上是Person.name
        print 'My name is %s'%(self.name); # -> class global name
        print 'name within class Person is actually the global name: %s'%(name); #-> whole global name
        print "only access Person's name via Person.name=%s"%(Person.name); # -> class global name

def selfAndInitDemo():
    persionInstance = Person("crifan");
    persionInstance.sayYourName();
    print "whole global name is %s"%(name); # -> whole global name

###############################################################################
if __name__=="__main__":
    selfAndInitDemo();