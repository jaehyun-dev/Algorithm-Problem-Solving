lv, jg = input().split()
arr = ['miss', 'bad', 'cool', 'great']
flag = 0
for i in range(4):
    if jg == arr[i]:
        flag = 1
        break
print(int(lv) * 200 * i if flag else int(lv) * 1000)