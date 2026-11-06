# # msg="Hello-Python"
# # for i in msg:
# #     print(i)
# # else:
# #     print("循环结束")
# #计算1-100之间所有奇数之和
# cnt=0
# for i in range(1,101):
#     if i%2!=0:
#         cnt+=i
# print("1-100之间所有奇数之和是：",cnt)
#
# #计算100-500之间所有3的倍数的数字之和
# total=0
# for j in range (100,501):
#     if j%3==0:
#         total+=j
# print("100-500之间所有3的倍数的数字之和是：",total)

# 嵌套循环
# n=int(input("请输入矩形的宽："))
# m=int(input("请输入矩形的长："))
# for i in range (n):
#     for j in range(m):
#         print("* ",end="")
#     print()

# 打印99乘法表
# for i in range(1,10):
#     for j in range (1,10):
#         if j<=i:
#             print(f"{j}*{i}={i*j} ",end="")
#     print()
#
# 猜数字小游戏
# import random
# num=random.randint(1,100)
# while True:
#     c = int(input("请输入一个1-100之间的数字："))
#     if c>num:
#         print("猜大了！")
#     elif c<num:
#         print("猜小了！")
#     else:
#         print("恭喜你，猜对啦！")
#         break
# else:
#     print("输入的数字有误！")
# print("随机生成的数字是：",num)

# 统计字符串
str="akiwksjakdiklowiqaamnv bamvaxnsjdsjkaaxkjd"
cnt=0
for i in str:
    if i=="a" or i=="k":
        cnt+=1
print(cnt)