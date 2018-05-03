# Python 3

"""
    1、掌握文件处理的流程及对应代码
    2、保存中文代码问题的处理
    3、使用with..as语句简化文件操作流程的代码
    4、掌握操作文件打开常用的格式
    5、完成一个文件读写的实战

"""

"""
1、打开文件
2、阅读/写入
3、关闭
"""

# 1、打开文件
# file = open('helloworld.txt','w',encoding='utf-8 ') # w是写入模式，若没有文件会自动创建
# file = open('helloworld.txt','r+',encoding='utf-8 ') # r+是读写模式，若没有文件会自动创建

# 2、阅读/写入
# file.write('Hello,World!,中文会乱码的话要设置打开文件时用encoding')
# print(file.readline()) # 读取

# 3、关闭
# file.close()

# 简化流程with..as语句
# with open('helloworld.txt','r+',encoding='utf-8 ') as f:
#     print(f.readline())


"""
1、接受用户输入，直到exit
2、追加方式 a a+
3、退出时候要显示记录的内容 break\exit
"""

while True:
    mystr = input("请输入信息：")
    if mystr in ["exit","quit"]:
        with open('helloworld.txt','r',encoding='utf-8') as f:
            for v in f:
                print(v,end='')
        break
    with open('helloworld.txt','a+',encoding='utf-8') as f:
        f.write(mystr+'\n')