# 创建元组
tup0 = ()  # 空元组
tup = ('Google', 'Baidu', 'Taobao', 'Wiki', 'Weibo', 'Weixin')

# 访问元组
print("tup[0]: ", tup[0])
print("tup[1:5]: ", tup[1:5])

# 修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组
# 元素值是不允许删除的，但可以使用del语句来删除整个元组
print(tup)
del tup
print("删除后的元组 tup : ")
# print(tup) # NameError: name 'tup' is not defined

# 运算符
# 与字符串一样，元组之间可以使用 +、+=和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
