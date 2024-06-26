# For 循环
for letter in 'Python':  # 第一个实例
    print("当前字母: %s" % letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果: %s' % fruit)

# 通过序列索引迭代
for index in range(len(fruits)):
    print('当前水果 : %s' % fruits[index])

# 循环使用 else 语句
for num in range(10, 20):  # 迭代 10 到 20 (不包含) 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)
