# # 定义集合
# s1={"C","D","X","D","O","U",50,50}
# print(s1)
# print(type(s1))
# s2=set()
#
# s={}#字典
#
# print(type(s))
# --------------------set()常用方法------------------------
#add():添加元素到集合
# s1={100,200,300,400,500}
# print(s1)
# s1.add(600)
# print(s1)
# # remove():移出集合中的指定元素--若不存在该元素那么就报错
# s1.remove(200)
# print(s1)
# # pop():随机删除集合中的元素并返回
# e=s1.pop()
# print(e)
# print(s1)
# # clear():清空集合
# s1.clear()
# print(s1)
#
# s2 = {"A", "B", "C", "D", "E", "X", "Y"}
# s3 = {"C", "E", "Y", "Z"}
#
# # difference() : 求两个集合的差集（存在于第一个集合，但不存在于第二个集合）
# print(s2.difference(s3))
# print(s3.difference(s2))
#
# # union() : 求两个集合的并集
# print(s2.union(s3))
# print(s2.union(s3))
#
# # intersection() : 求两个集合的交集
# print(s2.intersection(s3))
# print(s3.intersection(s2))


# 案例

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

print("同时选修了法语和艺术的名单为：",french_set & art_set)
print("同时选修了四门课程的学生有：",french_set.intersection(art_set.intersection(basketball_set.intersection(football_set))))
print("选修了足球，但是没有选修篮球的学生有：",football_set.difference(basketball_set))
# 3. 找出选修了足球，但是没有选修篮球的学生 - 差集
# 方式一：
fb_set = football_set.difference(basketball_set)
print(f"选修了足球，但是没有选修篮球的学生：{fb_set}")

# 方式二： - ----> 差集
fb_set2 = football_set - basketball_set
print(f"选修了足球，但是没有选修篮球的学生：{fb_set2}")

# 方式三：集合推导式 ----> 快速构建集合，语法：{要往集合中添加的数据 for s in set1 if 条件}
fb_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球，但是没有选修篮球的学生：{fb_set3}")

s4= football_set.union(basketball_set).union(french_set).union(art_set)
for i in s4:
    cnt=0
    if i in football_set:
        cnt += 1
    if i in basketball_set:
        cnt += 1
    if i in french_set:
        cnt += 1
    if i in art_set:
        cnt += 1
    print(f"学生{i}的选课数量为：{cnt}")

