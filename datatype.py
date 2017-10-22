# 列表 可修改元素内容
stuList = ["小明", "小华", "小宇", "小娟", "小云"]
print(stuList[3])
stuList[3] = "小月"
print(stuList[3])

# 元组 元素不可更改
stuStuple = ("小明", "小华", "小宇", "小娟", "小云")
print(stuStuple[1])

# 集合
a = set("abcmmaccddajggljf")
b = set("cdfm")

# 交集
x = a&b
print(x)
# 并集
print(a|b)
# 差集
print(a - b)
# 自动去除重复元素
print(a)
new = set(a)
print(new)

# dictionary
stuDict = {'name': 'weiwei', '籍贯': '成都'}
print(stuDict['name'])
print(stuDict['籍贯'])
# add to dictionary
stuDict['hobby'] = 'music'
print(stuDict)