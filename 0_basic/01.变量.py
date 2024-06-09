"""
在Python中，变量就是一个标识符，用于引用存储在计算机内存中的数据。
每个变量都有一个名称和关联的值，可以将值存储在变量中并在程序中多次使用。
"""
# 变量创建
# 创建无需关键字
name = "Fredo"
# 打印变量
print(name)
# 可以多次使用
print("Hello " + name)

# 修改变量值
name = "FUJW"
print(name)
#########################################
# 变量运算
x = 22
y = 13
print(x + y)  # 加，3
print(x - y)  # 减，9
print(x * y)  # 乘,286
print(x / y)  # 除，1.6923076923076923
print(x // y)  # 整除，1
print(x ** y)  # 幂，282810057883082752
print(x % y)  # 取余，9
#########################################
# 变量传递
a = 10  # 将10赋值给变量a
b = a  # 将变量a的值赋给变量b
a = 20  # 修改变量a的值为20
print(a)  # 20
print(b)  # 10
#########################################
# 表达式赋值
m = 100
m = m - 10
print(m)
#########################################
# 命名规范
# 1.见名知意
age = 20
# 2.驼峰或下划线，不能数字开头
stu_name1 = "Fredo"
stuName2 = "Fredo"
# 3.不能包含保留字
"""
Python的33个保留字如下：
False、None、True、and、as、assert、break、class、continue、
def、del、elif、else、except、finally、for、from、global、if、
import、in、is、lambda、nonlocal、not、or、pass、raise、return、
try、while、with、yield。
"""
# def="def"
