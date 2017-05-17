# coding:utf-8
list1 =[1,1]
list2 =[2,2]
list1.extend(list2)
print list1

print ' - '*10

q = 'a' in 'abc'
print q

book =['python','django',666]
print book
book.append(111)
print book
book.insert(1,'web')
print book
#print book*2
book.remove('web')
print book
book.pop(-1)
print book
book.extend(['extend','2333'])
print book

data =[x**2 for x in range(10) if x%3 == 0]
print data

shengchengqi = (x**2 for x in range(100) if x%3 == 0)
print shengchengqi

strs = 'django is wonderful wonderful'
words = strs.split()           #将字符串按空格切分成数组
print words
temp = ':::'.join(words)
print temp
w = temp.split(':::')         #将字符串按：：：切分成数组
print w

print strs.upper()            #全部转换为大写字母
print strs.isupper()          #判断是否全部为大写字母
print strs.upper().isupper()
print strs.title()            #将首字母转换为大写字母，以空格作为分割标志
print strs.capitalize()       #只将第一个单词的首字母大写
print strs.count('o')        #计算o在字符串中出现的次数
print strs.find('o')         #找到字母o第一次出现的位置
print strs.startswith('django')   #是否以指定字符串开头
print strs.endswith('ful')     #是否以指定字符串结尾
print strs.replace("wonful","great") #对全部匹配的字符串。查找替换，查找到，则替换，查找不到，则不替换也不报错
print strs.replace('wonderful','great')

hi = '''hi
you'''
print hi   #打印出来，也显示分行的效果


#元组是由逗号决定的，不是由小括号决定的。
b=('only-one')
print b[0:4]
b=('only-one',)
print b
print b[0]

zip_1 =[1,2,3]
zip_2 =('a','b','c')
print zip(zip_1,zip_2)

book_list ={'title': 'python web development','year': 2008}
for key in book_list:
    print key, ":",book_list[key]

print book_list.get('pub','N/A')
book_list['pub'] = 'girls bar'
print book_list
del book_list['pub']
print book_list
book_list.setdefault('pub','hot bar')
print book_list