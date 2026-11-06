# print("Hello")
# print(type("Hello"))
# print(type(10))
# print(type(True))
# print(type(False))
# print(type(None))
#常见数据类型 isinstance(数据，类型）返回bool值，判断是否是这个类型
# num=5.0
# print(isinstance(num,int))

#字符串
# s1="Hello" #双引号定义
# s2='Python' #单引号定义
# s3="""
# Hello:
#     欢迎大家
#     大家好
# """#三引号定义的字符串，可以定义多行字符串
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# #定义字符串
# msg1='It\'s very good'
# print(msg1)
# msg3="Hello的意思就是\"您好\""
# print(msg3)
# print("\t欢迎大家 \n\t大家好")#\n 换行   \t 缩进

#字符串拼接
# s1="人生苦短"+"我用Python"+",OK"
# print(s1)
#
# msg1="人生苦短"
# msg2="我用Python"
# print("龟叔说："+msg1+" , "+msg2)
#案例
name="郭祥熙"
age=18
pro="软件工程"
hobby="Python,Java"
print( "\"大家好，我是%s，今年%s岁，学习的专业是%s，爱好%s\"" %(name,age,pro,hobby) )
print( f"\"大家好，我是{name}，今年{age}岁，学习的专业是{pro}，爱好{hobby}\" " )

#占位符%
s1="郭导"
print("大家好，我是 %s ，欢迎大家" %s1)