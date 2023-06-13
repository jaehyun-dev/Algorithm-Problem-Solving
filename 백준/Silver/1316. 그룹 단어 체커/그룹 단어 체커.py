from collections import Counter
n = int(input())
count = 0
for _ in range(n):
    a = list(input())
    b = Counter(a)
    if b.most_common(1)[0][1] == 1:
        count += 1
    else:
        flag = True
        for i in list(b):
            num = b[i]
            if num > 1:
                index_ = a.index(i)
                for _ in range(num - 1):
                    a.remove(i)
                    if index_ != a.index(i):
                        flag = False
                        break
            if not flag:
                break
        if flag:
            count += 1
print(count)