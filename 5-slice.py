# Python 3

# 支持切片的：列表、元组、字符串
# 方法1.slice(start_index,end_index,step)
val = "zhanggaoxiang666"
s = slice(1,5) # 包含起始位置，不包含结束位置
print(val[s])

s = slice(1,5,2) # 加入步长
print(val[s])

# 方法2.sequence[start_index:end_index:step]
print(val[1:5])
print(val[1:5:2])

print(val[1::]) # 默认步长为1
print(val[:9:]) # 默认从第1个开始

# 负数切片是从右往左切，从最右边第一个开始为-1,往前逐个减小,步长为-1，倒叙
print(val[-1:-9:-1])
print(val[::-1]) # 倒序
print(val[4:0:-1])
