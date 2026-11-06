# day=int(input("请输入今天星期几："))
# match day:
#     case 1:
#         print("今天星期一")
#     case 2:
#         print("今天星期二")
#     case 3:
#         print("今天星期三")
#     case 4:
#         print("今天星期四")
#     case 5:
#         print("今天星期五")
#     case 6 | 7:
#         print("今天周末")
#     case _:
#         print("输入错误")
# 简易计算器
a=float(input("请输入第一个数字："))
b=float(input("请输入第二个数字："))
c=input("请输入运算符：")
match c:
    case "+":
        print(f"结果为：{a+b}")
    case "-":
        print(f"结果为：{a-b}")
    case "*":
        print(f"结果为：{a*b}")
    case "/" if b!=0:
        print(f"结果为：{a/b}")
    case _:
        print("输入有误")