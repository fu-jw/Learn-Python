# 创建字典
emptyDict1 = dict()
emptyDict2 = {}

tinydict = {'Name': 'Fredo', 'Age': 17, 'Class': 'First'}

# 访问字典
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])
# 如果用字典里没有的键访问数据，会输出错误
# print ("tinydict['Alice']: ", tinydict['Alice'])# KeyError: 'Alice'

# 修改字典
tinydict['Age'] = 18  # 更新 Age
tinydict['School'] = "清华大学"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显式删除一个字典用del命令
# del tinydict['Name']  # 删除键 'Name'
# tinydict.clear()  # 清空字典
# del tinydict  # 删除字典

# print("tinydict['Age']: ", tinydict['Age'])
# print("tinydict['School']: ", tinydict['School'])
