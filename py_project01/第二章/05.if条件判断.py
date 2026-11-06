# # score=700
# # if score>=680:
# #     print("欢迎来到清华读书")
# #     print("也恭喜你即将踏入精彩的大学生活")
# # print("---------------------------------------")
# zhanghao=int(input("请输入账号："))
# mima=int(input("请输入密码："))
# if zhanghao==18888888888 and mima==666888:
#     print("登陆成功，欢迎你")
# else:
#     print("账号或密码错误")

# 判断平年闰年
# years=int(input("请输入一个年份："))
# if years % 100 == 0:
#     if years % 400 ==0:
#         print(f"{years}是闰年")
#     else:
#         print(f"{years}是平年")
# else:
#     if years % 4 == 0:
#         print(f"{years}是闰年")
#     else:
#         print(f"{years}是平年")
#
# 输入三条边长
a = float(input("请输入边长a："))
b = float(input("请输入边长b："))
c = float(input("请输入边长c："))

# 2．判断三角形的类型 - pass 是一个空语句，起到一个语法占位的作用
if a + b > c and a + c > b and b + c > a: # 条件成立，构成三角形
    if a == b and b == c:
        print(f"{a} {b} {c} 这三个边长构成等边三角形 ~")
    elif a == b or b == c or a == c:
        print(f"{a} {b} {c} 这三个边长构成等腰三角形 ~")
    else:
        print(f"{a} {b} {c} 这三个边长构成普通三角形 ~")
else:
    print(f"{a} {b} {c} 这三个边长不能构成三角形！！！")
