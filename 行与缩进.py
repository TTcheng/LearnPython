# 3个物理行
print('abc')
print('123')
print('hello')

# 以下是1个物理行 3个逻辑行
print('xyz');print('789');print('Hi')
# 以下是1个逻辑行 3个物理行
print('''我
正在
学习python''')
# 以上是分号在一个物理行中将各个逻辑行隔开

# 行连接符号 \
print("人生苦短,\
我用Python")

# Python用缩进和冒号代替java 的{ }
a = 0
while a<3:
    print(a)
    a+=1
#java的写法如下
# a = 0;
# while (a<3)
# {
#     println(a);
#     a+=1;
# }