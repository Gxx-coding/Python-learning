# #导入模块
# import Utils.my_fun
# Utils.my_fun.log_separator2()
#

# from Utils import my_fun
# my_fun.log_separator1()

# 注意：如果要通过这种形式访问模块，需要在utils里的__init__中添加__all__=[]
from Utils import *
my_fun.log_separator1()
print(my_var.PI)
#导入模块中的功能
from Utils.my_fun import *
log_separator1()