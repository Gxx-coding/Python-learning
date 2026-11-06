# # 列表操作
# s=[56,90,88,90,'a',"Hello",True]
# print(type(s))
# # 访问列表的元素
# # 获取
# print(s[0])
# print(s[-7])
# # 修改
# s[5]='abc'
# print(s)
# # 删除
# del s[6]
# print(s)
# # 遍历
# for item in s:
#     print(item)

# ---------------------列表list切片-----------------------------
# s=["A","C","H","K","L","B","D","X","C","U"]
# print(s[0:5:1])
# print(type(s[0:5:1]))
# print(s[0:5:2])

# ---------------------列表list常用方法-----------------------------
# 列表定义
# s=[56,90,88,65,90,100,209,72,145]
# # append在列表尾部追加元素
# s.append(108)
# print(s)
# # insert在指定索引之前插入元素
# s.insert(0,111)
# print(s)
# # remove移出遇到的第一个元素
# s.remove(90)
# print(s)
# # pop删除列表中指定索引位置的元素并返回
# e=s.pop(2)
# print(e)
# # sort对列表进行排序
# s.sort()
# print(s)
# # reverse反转列表元素
# s.reverse()
# print(s)

# 案例1
# a=[]
# cnt=0
#
# for i in range(0,10):
#     s = float(input("请输入一个有效的数字："))
#     a.append(s)
#     cnt+=s
# # print(type(a))
# # print(a)
# a.sort()
# print("最小值为：",a[0])
# print("最大值为：",a[-1])
# ans=cnt/10
# print("平均值为：",ans)
# print("平均值为：",sum(a)/len(a))

# 案例2
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# num_list3=[]
# num_list4=num_list1+num_list2
# for i in num_list4:
#     if i not in num_list3:
#         num_list3.append(i)
# print(num_list3)

# 案例3
list1=[]
list2=[]
for i in range(1,21):
    list1.append(i*i)
for j in range(1,21):
    if j%2==0:
        list2.append(j*j)
print(list1)
print(list2)

# 列表推导式
list1 = [i*i for i in range(1,21)]
list2 = [j*j for j in range(1,21) if j%2 == 0]
print(list1)
print(list2)
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98]
num_list2=[k**2 for k in num_list if k%2==0]
print(num_list2)
