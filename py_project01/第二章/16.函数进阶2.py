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