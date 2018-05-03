# Python 3

# 捕获异常

"""
try:
    要捕获的代码
except 异常名(不写表示所有异常):
    如果在try部分引发了XX异常
except 异常名,数据:
    如果引发了XX异常,获取附加的数据
else:
    如果没有异常发生
finally:
    始终会被执行到的代码
"""

try:
    # int('fff')
    print(aaa)
except ValueError as e:
    print("处理了异常:",e)
except NameError as e:
    print('处理了异常：',e)
except:
    print('有其他异常')

# 手动抛出异常
# raise TypeError