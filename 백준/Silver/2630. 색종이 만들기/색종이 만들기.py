import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

def check(arr):
    flag = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[0][0]:
                flag = False
                break
        if not flag:
            break
    if flag:
        return [arr[0][0]]
    else:
        arr_0 = []
        for i in range(len(arr)//2):
            temp = []
            for j in range(len(arr)//2):
                temp.append(arr[i][j])
            arr_0.append(temp)
        arr_1 = []
        for i in range(len(arr)//2):
            temp = []
            for j in range(len(arr)//2, len(arr)):
                temp.append(arr[i][j])
            arr_1.append(temp)
        arr_2 = []
        for i in range(len(arr)//2, len(arr)):
            temp = []
            for j in range(len(arr)//2):
                temp.append(arr[i][j])
            arr_2.append(temp)
        arr_3 = []
        for i in range(len(arr)//2, len(arr)):
            temp = []
            for j in range(len(arr)//2, len(arr)):
                temp.append(arr[i][j])
            arr_3.append(temp)
        return [check(arr_0), check(arr_1), check(arr_2), check(arr_3)]


temp = check(arr)
flag = True
while flag:
    flag = False
    for i in temp:
        if type(i) != int:
            flag = True
            break
    ans = []
    for i in temp:
        if type(i) == list:
            ans.extend(i)
        else:
            ans.append(i)
    temp = ans

print(ans.count(0))
print(ans.count(1))