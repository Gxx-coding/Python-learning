# # 函数定义
# def out_line():
#     print("-------------")
# # 函数调用
# # out_line()
# # 计算圆形的面积
# def circle_area(r):
#     return 3.14*r*r
# area1=circle_area(10)
# print(area1)
# # 计算长方形的面积
# def rectangle_area(a,b):
#     return a*b
# area2=rectangle_area(10,20)
# print(area2)
# # 函数3：计算圆的面积，周长 -- 半径 -----> 如果返回值有多个，多个返回值之间逗号分隔
# def circle_area_len(r):
#     """
#     该函数用于根据圆的半径，计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积，圆的周长
#     """
#     return 3.14 * r * r, round(2 * 3.14 * r,1)
#
# al = circle_area_len(10)
# print(al)
# help(circle_area_len)

# 函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")


def function_b():
    print("b ... before")
    function_c()
    print("b ... after")


def function_c():
    print("c ...")


function_a()

print("函数调用完毕 ~")

# 案例
# 计算三角形面积
def triangle_area(a,h):
    return a*h/2
# 计算传入字符串中元音字母的个数
def aeiou_num(s):
    return s.count("a")+s.count("e")+s.count("i")+s.count("o")+s.count("u")+s.count("A")+s.count("E")+s.count("I")+s.count("O")+s.count("U")
# 计算传入班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留一位小数），并返回
# def score(stu:list):
#     stu.sort()
#     count=0
#     cnt=0
#     for i in stu:
#         count+=i
#         cnt+=1
#     ave=count/cnt
#     mn=stu[0]
#     mx=stu[cnt-1]
#     return mx,mn,round(ave,1)
def score(stu: list):
    if not stu:
        return None, None, None

    mx = max(stu)
    mn = min(stu)
    ave = sum(stu) / len(stu)

    return mx, mn, round(ave, 1)
