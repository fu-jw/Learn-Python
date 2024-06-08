# 整型
x = 20
y = -10
print(x + y)
#################################
# 浮点型
a = 3.14
b = -1.01
print(a - b)
#################################
# 布尔型
c = 2 > 1
d = 2 < 1
e = 2 != 1
print(c)  # True
print(d)  # False
print(e)  # True

# 内置函数bool(),返回该变量的布尔值
print(bool(d))  # False
# 注意：只有零为False，非零为True
print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True
print(bool("0"))  # True
#################################
# None型
# 在Python中，None是一个特殊的常量，表示缺少值或空值。
# 常用于表示函数无返回值或变量尚未被赋值的时候

# 1.函数返回值为空，常见 print()
ret = print("Hello World")
print("ret: ", ret)  # ret:  None
print(type(ret))  # <class 'NoneType'>

# 2.变量初始值
num1 = int(input("num1: "))
num2 = int(input("num2: "))
opt = input("操作符：")
ans = None  # 初始化变量

if opt == "+":
    ans = num1 + num2
elif opt == "-":
    ans = num1 - num2
elif opt == "*":
    ans = num1 * num2
elif opt == "/":
    ans = num1 / num2
else:
    print("非法操作！")

# 不初始化时，可能报错：NameError: name 'ans' is not defined
print(ans)
