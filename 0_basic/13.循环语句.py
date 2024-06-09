# While 循环

count = 0
while count < 9:
    print("The count is:", count)
    count = count + 1
print("While 循环结束了")

# continue 用于跳过该次循环，
# break 则是用于退出循环
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# while … else 在循环条件为 false 时执行 else 语句块
count = 0
while count < 5:
    print(count), " is  less than 5"
    count = count + 1
else:
    print(count), " is not less than 5"

