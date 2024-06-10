# 创建列表
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 访问其中数据
print(list[0])
print(list[2])
print(list[-1])
print("list[1:-2]: ", list[1:-2])

# 更新列表
print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list.append('Baidu')
print("更新后的列表 : ", list)

# 删除列表元素
print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

# 列表比较
# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

# 常见函数
