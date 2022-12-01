n = int(input())

def han(num):
    n = str(num)
    if len(n) <= 2:
        return True
    else:
        i = 0
        while i < len(n):
            d = int(n[i]) - int(n[i + 1])
            if int(n[i + 1]) - int(n[i + 2]) == d:
                i += 1
            else:
                return False
                break
            return True

arr = []
for i in range(1, n + 1):
    if han(i):
        arr.append(i)

print(len(arr))