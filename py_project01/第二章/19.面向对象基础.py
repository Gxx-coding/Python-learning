# #定义类
# class Car:
#     pass
# #创建对象
# c1=Car()
# # 动态的为对象添加属性
# c1.color="red"
# c1.brand="BMW"
# c1.name="X5"
# c1.price=500000
# print(c1)
# print(c1.__dict__)#将对象中所有属性以字典的形式输出出来

# 定义类
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
        print("初始化完毕")

    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price
    def running(self):
        print(f"{self.brand}{self.name}正在马路上飞驰")
    def total_cost(self,discount,rate=0.1):
        """
        计算提车的总费用并返回
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        return self.price * discount + self.price*rate

# 实例化对象
c2=Car("BMW","X5",500000)
print(c2.__dict__)
c2.running()
print(f"{c2.brand}{c2.name}的价格为{c2.total_cost(0.7,0.1):.1f}元")

c3=Car("BMW","X5",600000)
print(c3)
print(c3.__eq__(c2))
print(c2.__lt__(c3))

print(c2==c3)
print(c2<c3)