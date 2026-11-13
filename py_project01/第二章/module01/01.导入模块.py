#导入模块 调用方式：模块名.功能名
#import random
import random as rd
for i in range(1,100):
    print(rd.randint(1,100))
# 导入模块中的功能 调用方式：功能名
# from random import randint
# from random import randint as rint
from random import *
for i in range(1,100):
    print(randint(1,100))