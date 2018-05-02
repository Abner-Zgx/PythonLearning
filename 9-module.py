# Python 3

# 模块：一个py文件就是一个模块
# 包：默认包含_init__.py的文件夹

# 导入包，首先创建一个包，然后包会默认执行_init_.py，因此，要在_init_.py中导入modulePackage.moduleTest

# import modulePackage
# print(modulePackage.moduleTest.test)

# import可以导入
from  modulePackage import  moduleTest
print(moduleTest.test)