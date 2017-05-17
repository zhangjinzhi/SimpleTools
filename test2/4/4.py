# -*- coding: UTF-8 -*-
if True:
     print "Answer"
     print "True"
else:
     print "Answer"
    # 没有严格缩进，在执行时保持
     print "False"

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
total = miles + \
        miles
print total

import sys;x = 'runoob'; sys.stdout.write(x + '\n')

a = b = c = 1
print a,b,c
a, b, c = 1, 2, "john"
print a,b,c

var1 = 1
var2 = 10          #删除后，该对象就不存在了。所以没法打印
print var1,var2
del var1
print var2
del var2


str = 'Hello World!'
print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print str[2:5] # 输出字符串中第三个至第五个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict ;print tinydict # 输出完整的字典# 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值

print
a = 21.0
b = 10.0
print a/b
print a%b
print a//b
print
a = 21
b = 10
print a/b
print a%b
print a//b

print
#and or not 是逻辑运算符

# in      not in 是判断是否在序列中
'''除了以上的一些运算符之外，Python还支持成员运算符，
测试实例中包含了一系列的成员，包括字符串，列表或元组'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "1 - 变量 a 在给定的列表中 list 中"
else:
   print "1 - 变量 a 不在给定的列表中 list 中"

if ( b not in list ):
   print "2 - 变量 b 不在给定的列表中 list 中"
else:
   print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if ( a in list ):
   print "3 - 变量 a 在给定的列表中 list 中"
else:
   print "3 - 变量 a 不在给定的列表中 list 中"

#身份运算符用于比较两个对象的存储单元
a = 20
b = 20
if ( a is b ):
   print "1 - a 和 b 有相同的标识"
else:
   print "1 - a 和 b 没有相同的标识"

if ( id(a) == id(b) ):
   print "2 - a 和 b 有相同的标识"
else:
   print "2 - a 和 b 没有相同的标识"


num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print 'hello'
else:
	print 'undefine'
# 输出结果

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果
var = 100
if ( var  == 100 ) : print "变量 var 的值为100"  #也可以在一行

# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter
print "Good bye!"

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:global Money
   global Money
   Money = Money + 1

print Money
AddMoney()
print Money

print globals()
print locals()

# 打开一个文件,如果没有，则创建一个新文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name,"\n"
fo.write( "www.runoob.com!\nVery good site!\n");
fo = open("foo.txt", "r+")
str = fo.read();
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()

import os
# 删除一个已经存在的文件test2.txt
os.remove("foo.txt")
# 创建目录test