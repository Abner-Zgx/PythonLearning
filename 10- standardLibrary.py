
# 时间
import time

now_time = time.localtime()
print(now_time)
print(now_time.tm_year)

print("today:"+str(now_time.tm_year)+"-"+str(now_time.tm_mon)+"-"+str(now_time.tm_mday))
print(time.strftime("%Y-%m-%d-%H-%M-%S",now_time))


import os
print(os.path.abspath("9-module.py"))
print(os.path.basename("/Users/xiang/PycharmProjects/untitled/9-module.py"))
print(os.path.splitext("9-module.py"))

# 生成目录
os.mkdir("testMakeDir")