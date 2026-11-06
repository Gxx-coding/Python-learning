# # 定义元组
# t1=(80,95,78,50,76,80,85,20)
# print(t1)
# print(type(t1))
# # 索引访问
# print(t1[0])
# print(t1[-1])
# # 切片
# print(t1[0:3:2])
# # count()统计元素的个数
# c=t1.count(80)
# print(c)
# # index()得到元素的索引（第一个元素)
# n=t1.index(80)
# print(n)
#
# # 注意点: 如果定义单元素的元组, 单个元素之后需要加上逗号, 比如 (100,)
# t2 = ()
# print(t2)
# print(type(t2))
#
# t3 = (100,)
# print(t3)
# print(type(t3))

# 组包与解包
# 组包----定义元组
# t1=(5,7,9,1)
# t2=5,7,9,1
# print(type(t2))
# # 基础解包
# a,b,c,d=t1
# # print(a)
#
# # (*)扩展解包----*收集剩余的所有元素，封装到列表list当中
# x,*y,z=t2
# s,*o=t2
# print(s)
# print(o)
# # *o,e=t2

# 案例
# a=10
# b=20
# # t1=(10,20)
# # b,a=t1
# a,b=b,a
# print(a)
# print(b)
#
# a=100
# b=200
# c=300
# c,a,b=a,b,c
# print(a)
# print(b)
# print(c)

# 案例
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 1. 计算每个学生的总分、各科平均分，然后一并输出出来。
# 方式一
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:  # ("S001", "王林", 85, 92, 78)
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

# 方式二:元组解包
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id,name,Chinese,Math,English in students:  # ("S001", "王林", 85, 92, 78)
    total = Chinese + Math + English
    avg = total / 3
    print(f"{id} \t {name} \t {Chinese} \t {Math} \t {English} \t {total} \t {avg:.1f}")

# 2. 统计各科成绩的最低分、最高分、平均分，并输出。

# a1=[]
# a2=[]
# a3=[]
# s1=0
# s2=0
# s3=0
# for t in students:
#     a1.append(t[2])
#     s1+=t[2]
#     a2.append(t[3])
#     s2+=t[3]
#     a3.append(t[4])
#     s3+=t[4]
# a1.sort()
# a2.sort()
# a3.sort()
# print(f"语文的最低分为{a1[0]},最高分为{a1[9]},平均分为{s1/10}")
# print(f"数学的最低分为{a2[0]},最高分为{a2[9]},平均分为{s2/10}")
# print(f"英语的最低分为{a3[0]},最高分为{a3[9]},平均分为{s3/10}")


# 2．统计各科成绩的最低分、最高分、平均分，并输出。
# 2.1 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

# 2.2 统计各科成绩的最低分、最高分、平均分，并输出。
print(f"语文最低分：{min(chinese_scores)}，最高分： {max(chinese_scores)}，平均分： {sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分：{min(math_scores)}，最高分： {max(math_scores)}，平均分： {sum(math_scores)/len(math_scores)}")
print(f"英语最低分：{min(english_scores)}，最高分： {max(english_scores)}，平均分： {sum(english_scores)/len(english_scores)}")

# 3. 查找成绩优秀（平均分大于90）的学生，并输出。
for s in students:  # ("S001", "王林", 85, 92, 78)
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg>90:
        print(f"{s[0]}{s[1]}同学的成绩优秀")
