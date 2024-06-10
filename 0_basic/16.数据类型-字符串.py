var1 = 'Hello World!'
var2 = "Python"

# 访问字符串中的值
print("var1[0]: ", var1[0])
print("var1[1:7]: ", var1[1:7])  # [1,7) 左闭右开
print("var1[:7]: ", var1[:7])  # 前7个
print("var1[2:]: ", var1[2:])  # 从2开始后面所有

print("var1[1:8:2]: ", var1[1:8:2])  # el o,从1到8，步长位2
print("var1[::2]: ", var1[::2])  # HloWrd,步长为2，隔一个字符输出
print("var1[::-1]: ", var1[::-1])  # !dlroW olleH, 倒序输出所有
print("var1[-1:-7:-1]: ", var1[-1:-7:-1])  # !dlroW,从右到左,范围:[-1,-7],倒序输出

# 字符串连接
print(var1[:6] + var2)

# 转义字符, 反斜杠

# 格式化
print ("我叫 %s 今年 %d 岁!" % ('Fredo', 20))

# 三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)