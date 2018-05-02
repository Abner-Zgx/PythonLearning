# Python 3

myName = "zgx6"

i = 0
while i < len(myName):
    print(myName[i])
    i += 1
    if myName[i-1] == "x":
        print("it is x")
        break
else:
    print("循环结束")

print("---------------划分线-----------------")

a = 0
while a < len(myName):
    print(myName[a])
    a += 1
    if myName[a-1] == "x":
        print("it is x")
        continue
else:
    print("循环结束")

# break 跳出内存循环
# continue 跳出当前
# exit()是退出整个程序