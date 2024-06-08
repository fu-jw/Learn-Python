num1 = input("输入num1：")  # 1
num2 = input("输入num2：")  # 2
print(num1 + num2)  # 12, Why???

# 因为input的输出值为字符串，结果就是字符串的拼接
# 此时需要进行类型转换！！！

# 将字符串转换成整型,int()
print(int(num1) + int(num2))

# 或如下：
# num1 = int(num1)
# num2 = int(num2)
# print(num1 + num2)

# 将字符串转换成浮点型,float()
print(float(num1) + float(num2))  # 3.0

# 将整型转换成字符串, str()
age = 20
print("age: " + str(age))  # age: 20

# 字符转数字型时，需要注意：
price1 = "100元"  # 1.含有非数字不能转
# print(int(price1))# ValueError: invalid literal for int() with base 10: '100元'

price2 = "103.25"  # 2.有小数点能转浮点型，不可转整型
# print(int(price2))# ValueError: invalid literal for int() with base 10: '103.25'
