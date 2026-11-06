# s="Hello-Python"
# print(s[4])
# print(s[-8])
# for i in s:
#     print(i)
# # 切片
# print(s[0:5:])
# print(s[:5])
# print(s[-1:-7:-1])
# print(s[::-1])


# s="Hello-Python-Hello-World"
# # find()查找指定字符串第一次出现的索引位置
# index=s.find("Python")
# print(index)
# # count()统计子字符串在指定字符串中出现的次数
# c=s.count("o")
# print(c)
# # upper（）转为大写
# su=s.upper()
# print(su)
# # lower()转为小写
# lo=s.lower()
# print(lo)
# # split()将字符串按照指定字符串切割为列表
# slist=s.split("-")
# print(slist)
# # strip()去掉字符串两端的空格
# ss=s.strip()
# print(ss)
# # replace()将字符串中的指定子串替换为新的内容
# sr=s.replace("-","_")
# print(sr)
# # startswith（）/endswith（）判断字符串是否以指定的字符串开头/结尾，返回布尔值
# print(s.startswith("Hello"))
# print(s.endswith("Python"))

# 案例
s=input("请输入您的邮箱")
if s.count("@")==1 and s.count(".")>=1:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")