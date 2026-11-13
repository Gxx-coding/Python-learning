# 常量
PI = 3.1415926
NAME = "黑马☆gxx"

def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

__all__=["log_separator1","log_separator2","PI"]
# 测试函数
if __name__=="__main__":
    print(__name__)
    log_separator1()


