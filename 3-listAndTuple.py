# Python 3

# List:列表
a = [1,2,3,4,5,6]
print(type(a))
print(a)
print(a[0])
print(a[1:3])

# 替换
a[0] = 0
print(a)

# 插入
a.append(7)
print(a)

# 删除
del a[1]
print(a)

# 删除
a.remove(3)
print(a)

# 长度
b = len(a)
print(b)

# 加法
c = a + [9,9]
print(c)

# 乘法（复制列表n次）
d = a * 3
print(d)

# 列表推导式
g = [1,2]
h = "hello world"
j = [i for i in h]
print(j)

# Tuple:元组
e = (1)
f = (1,) # 注意要加逗号，否则不是元祖
print(type(e))
print(type(f))
print(f[0])
print(len(f))

# 其他申明方式
x = list()
print(type(x))

y = tuple()
print(type(y))