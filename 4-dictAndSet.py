# Python 3

# 字典
a = {}
b = dict()
print(type(a))
print(type(b))

c = {'力量':2,'智力':3}
print(c['力量'])
c['智力'] = 10
print(c['智力'])

# 删除
del c['智力']
print(c)

# 修改
c['速度'] = 11
print(c)

# 长度
print(len(c))

# 字典中的键必须是不可变对象（比如可以是元组（元组不可变），但不可以是列表（列表可变））
c[('智力','速度')] = 11
print(c)

# 集合（声明的时候必须有值）
a = {1,2,3}
b = set()
print(type(a))
print(type(b))

# 添加add
b.add('abc')
print(b)

# 添加update
b.update('1234')
print(b)

# 判断是否在集合中
c = '3' in b
print(c)

# 交并差
d = set()
d.update('345')
print(d)

# 交集
e = b & d
print(e)

# 并集
f = b | d
print(f)

# 差集
g = b - d
print(g)

