# # 字典--key不能重复,如果重复，那么后面的值会覆盖前面的值，key必须得是不可变类型
# # 定义字典
# dict1={"王淋":670,"李沐晚":480,"徐立国":680,"韩立":688}
# print(dict1)
# print(type(dict1))
#
# # dict2 = {0:670, 1.5:608, (1,2):580, ['A','B']:688}
# # print(dict2)
#
# #访问
# print(dict1["王淋"])
#
# # 字典 常见操作
# dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["涛哥"] = 620
# print(dict1)
#
# # 查询
# print(dict1["涛哥"])        # 根据key获取value，key不存在会报错
# print(dict1.get("涛哥"))    # 根据key获取value，key不存在返回None，不会报错
#
# print(dict1.keys())    # 获取所有的key（键）
# print(dict1.values())  # 获取所有的value（值）
# print(dict1.items())   # 获取所有的键值对
#
# # 删除 pop：根据key删除，返回被删掉的值
# score = dict1.pop("许立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
from os.path import exists
from tkinter.font import names

# 案例：
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车

shopping_cart={}
print("欢迎使用购物车管理系统 ~")

menu = """
########## 购物车系统 ##########
#        1. 添加购物车         #
#        2. 修改购物车         #
#        3. 删除购物车         #
#        4. 查询购物车         #
#        5. 退出购物车         #
################################
"""
while(True):
    print(menu)
    choice=input("请选择要执行的操作（1-5）：")
    match choice:
        case "1":#添加
            goods_name=input("请输入商品名称：")
            goods_price=float(input("请输入商品价格："))
            goods_number=int(input("请输入商品数量："))
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择")
            else:
                shopping_cart[goods_name]={"price":goods_price,"number":goods_number}
                print("添加成功，商品信息为：",shopping_cart[goods_name])
        case "2":#修改
            goods_name = input("请输入商品名称：")
            if goods_name in shopping_cart:
                goods_price = float(input("请输入商品价格："))
                goods_number = int(input("请输入商品数量："))
                shopping_cart[goods_name] = {"price": goods_price, "number": goods_number}
                print("修改成功，修改后的商品信息为：",shopping_cart[goods_name])
            else:
                print("修改失败，该商品不存在！")
        case "3":#删除
            goods_name = input("请输入商品名称：")
            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
                print("删除成功！")
            else:
                print("删除失败，该商品不存在！")
        case "4":#查询
            if shopping_cart != {}:
                for name, info in shopping_cart.items():
                    print(f"商品名称：{name}，商品价格：{info['price']}，商品数量：{info['number']}")
            else:
                print("购物车为空！")
        case "5":#退出
            print("欢迎下次使用！")
            break
        case _:
            print("输入有误，请重新输入！")
            pass



