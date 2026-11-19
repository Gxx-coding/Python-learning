class Shopping_cart:
    def __init__(self,name,price,num):
        self.name=name
        self.price=price
        self.num=num
    def __str__(self):
        return f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.num}"



class ShopManagement:
    shopping_cert=[]
    system_version="1.0"
    system_name="购物车管理系统"
    #添加购物车
    def add_shopping(self):
        name = input("请输入商品名称")
        price = float(input("请输入商品价格"))
        num = int(input("请输入商品价格"))
        for s in self.shopping_cert:
            if s.name == name:
                print("该")
    #修改购物车
    def change

    #删除购物车

    #查询购物车

    #退出购物车
