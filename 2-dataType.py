# Python 3

# 基本数据类型
# Number:数字(int、float、bool、complex(复数))
# String:字符串
# List:列表
# Tuple:元组
# Set:集合
# Dictionary:字典

# Number:数字
a = 100
print(type(a))

b = 10.1
print(type(b))

c = True
print(type(c))

d = 3+2j
print(type(d))

# 类型转换
e = str(a)
print(type(e))

f = float(a)
print(type(f))

# String:字符串
g = 'test'
h = "test"
i = """我是一个很长的字符串，用三引号可以
    换行等等，很方便"""
print(i)

j = "你好，"+"我是张高翔"+",试一下➕号拼接字符串"
print(j)

# 如何让转义字符\n输出，只要再加一个\即可
k = "aaa\nbbb\nccc\n"
l = "aaa\\nbbb\\nccc\\n"
m = r"aaa\nbbb\nccc\n"
print(k)
print(l)
print(m)

# 格式化字符串
n = "%s好，我是%s,今年%s岁" % ("翔哥","翁翁","18")
o = "{}好，我是{},今年{}岁".format("翔哥","翁翁","18")
p = "{1}好，我是{0},今年{2}岁".format("翔哥","翁翁","18")
q = "{1}好，我是{0},今年{2:d}岁".format("翔哥","翁翁",18)
print(n)
print(o)
print(p)
print(q)