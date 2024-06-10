# 集合（set）是一个无序的不重复元素序列
# 元素不会重复，并且可以进行交集、并集、差集等常见的集合操作
# 使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 添加元素
basket.add('peach')
print(basket)
# 移除元素
basket.remove('peach')
print(basket)

# 集合个数
print(len(basket))
