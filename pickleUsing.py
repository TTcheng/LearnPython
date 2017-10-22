# pickle 腌制
import pickle

# dumps(objects)将对象序列化
print("创建列表listA...")
listA = ["I","like","apple"]
print('正在将listA序列化存储在变量listB中...')
listB = pickle.dumps(listA)
print('这是listB中的内容：%s'%listB)

# loads(string) 将对象恢复 并且对象类型也恢复
print('正在从listB中加载listA...')
listC = pickle.loads(listB)
print('这是listA的内容 {0}'.format(listC))
print()

# dump(obj,file)将对象序列化存储在文件中
group1 = ("I","love","you")
print("创建元组group1...")
f1 = open('1.pk1','wb')
pickle.dump(group1,f1,True)
print('正在将group1序列化存储在文件%s中...' % f1.name)
f1.close()

# load(obj,file) 将文件里面的数据恢复
f2 = open('1.pk1','rb')
print('正在从文件1.pk1中加载group1...')
t = pickle.load(f2)
print('这是group1的内容 {0}'.format(t))
f2.close()