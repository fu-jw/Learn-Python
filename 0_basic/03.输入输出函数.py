# input函数
# 接收用户从控制台的输入信息，并返回字符串
name = input("Enter your name: ")
print(name)

age = input("Enter your age: ")
print(age)
# print(age+10),报错：TypeError: can only concatenate str (not "int") to str
print(int(age) + 10)  # 必须进行类型转换才可以
##########################################
# print函数
# 在控制台打印信息
height = 180
# 默认包含换行
print(name)
print(age)
print(height)
# 可以去除换行符
print(name, end=" ")
print(age, end=" ")
print(height)

# 可以一行打印多个值，默认空格分割
print(name, age, height)  # fjw 20 180
# 可以修改分隔符
print(name, age, height, sep=";")  # fjw;20;180

print("height: ", height)  # height:  180
