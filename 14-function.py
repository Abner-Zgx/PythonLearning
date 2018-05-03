# Python 3

def myfunc(name,age="18"):
    print(name+"666"+"，年龄："+age)

myfunc(name="翔哥")
myfunc("翔哥","20")

def myfunc2(name,age="18",*args,**kwargs): #*args可变参数
    print(args)
    print(type(args)) # 元组可变参数

    print(kwargs)
    print(type(kwargs)) # 字典可变参数
    return 100

myfunc2("翔哥","10",19,20,21,sex="男",live="上海")

result = myfunc2("我","99")
print(result)

# 匿名函数（较少用，可以简化冗余代码）
(lambda : print("这是一个匿名函数")) ()
print(type((lambda : print("这是一个匿名函数"))))

# 了解内置函数 用dir(__builtins__)

print(dir(__builtins__))