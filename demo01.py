"""
print("hello world!")#字符串
print(2333)#整数
print(2.333)#小数
print(True)#布尔值  True False
print(())#元组
print([])#数组
print({})#字典


多行注释三个引号
锄禾日当午

print("haha",2333,2.3333)
print("哈哈"+"嘻嘻")#字符串的拼接
print("哈哈"*10)
print(((1+2)*100-9.9)/2)
print(2>3)
print(2<3)

#变量
#赋值
name ="张三" #把张三这个值赋值给了名字叫name的这个变量
print(name)
"""
# a = input("请输入：")
# b = input("请输入：")
# print("input获取的内容：",a+b)

#数据格式的转换

# print(type("哈哈"))
# print(type(300))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = int(input("请输入："))
# b = int(input("请输入："))
# print("input获取的内容：",a+b)


#元组,下标,从0开始编号
# a = (1,2,3,4,'哈哈','哈哈','哈哈','哈哈','嘻嘻',True,False)
# print(a[3])
# 切片
# print(a[0:4])#左闭右开
# print(a[4:9])
# print(a[9:])
# print(a[-3:])

# print(a.index('嘻嘻'))
# print(a.count('哈哈'))

#二维元组
# b = (a,'哈哈',"芜湖")
# print(b[0][3])

# a = [1,2,3,4,'哈哈','哈哈','哈哈','哈哈','嘻嘻',True,False]
# print(a[4])
# #元组写好了不能修改，数组是可以修改的
# a.append("append1")
# a.append("append2")
# a.insert(0,'insert')
# print(a)

# b = a.pop(1)#剪切
# c = a.pop(1)
# print(b+c)
# print(a)
# print(b)

"""
python的语法
所有的方法都是小括号结尾，比如print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如 a[0]
元组、数组、字典的定义，分别是(),[],{}
"""
"""
字典的特点
1、字典中的值没有顺序
2、字典的结构必须是 键值对的结构。 key:value
3、字典的取值，是通过key去取值这个value
"""
a = {
    'name':'张三',
    0:'哈哈',
    'age':25
    }

#取值
print(a['name'])
#新增
a['high'] = '183cm'
print(a)
#修改
a['name'] = '李四'
print(a)

#数组和字典的删除
del a['name']
print(a)
