# 函数的参数类型
# 加
def add(x,y):
    return x+y
# 减
def subtract(x,y):
    return x-y
# 乘
def multiply(x,y):
    return x*y
# 除
def devide(x,y):
    return x/y
# 计算
def calc(x,y,oper):
    return oper(x,y)

print(calc(20,10,add))
print(calc(20,10,subtract))
print(calc(20,10,devide))
print(calc(20,10,multiply))


# 匿名函数
# 打印一个分割线
outline=lambda : print("-------------")

# 计算两个数字之和
add=lambda a,b: a+b
outline()
print(add(10,30))

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)
data_list.sort(key= lambda item:len(item),reverse=False)
print(data_list)


# 案例1：n的阶乘
def jiecheng(n):
    if n==1:
        return n
    else:
        return n*jiecheng(n-1)

print(jiecheng(5))

"""
案例2：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
具体规则如下：
    1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
    2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def caul_order_cost(*args: tuple[str,float,int],coupon=0,score=0,express=0)-> float:
    """

    :param args: 商品信息（商品名、价格、数量）
    :param coupon:优惠券
    :param score:积分抵扣
    :param express:运费信息
    :return:订单的总金额
    """
#     订单总金额=商品总价 - 优惠金额 - 积分抵扣金额 + 运费
#     1.商品总价
    goods_price = [goods[1]*goods[2] for goods in args]
    total_price = sum(goods_price)
#     2.优惠金额
    if total_price>=5000 and coupon<=total_price:
        total_price-=coupon
#     3.积分抵扣金额
    if total_price>=5000 and score//100 <=total_price:
        total_price-= score//100
#     4.运费
    total_price+=express
    return total_price
print(caul_order_cost(("鼠标",1999,1),("键盘",3999,2),coupon=1000,score=1500,express=1))
print(caul_order_cost(("鼠标",1999,1),("键盘",3999,2),express=9.9))











