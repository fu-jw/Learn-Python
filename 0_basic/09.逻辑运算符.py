a = 10
b = 20

if a and b:
    print("1 - 变量 a 和 b 都为 True")
else:
    print("1 - 变量 a 和 b 有一个不为 True")

if a or b:
    print("2 - 变量 a 和 b 都为 True，或其中一个变量为 True")
else:
    print("2 - 变量 a 和 b 都不为 True")

# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 True")
else:
    print("3 - 变量 a 和 b 有一个不为 True")

if a or b:
    print("4 - 变量 a 和 b 都为 True，或其中一个变量为 True")
else:
    print("4 - 变量 a 和 b 都不为 True")

if not (a and b):
    print("5 - 变量 a 和 b 都为 False，或其中一个变量为 False")
else:
    print("5 - 变量 a 和 b 都为 True")
