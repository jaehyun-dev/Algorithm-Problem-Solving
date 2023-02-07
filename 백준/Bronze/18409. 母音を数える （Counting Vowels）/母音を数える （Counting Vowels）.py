N = int(input())
S = input()
count = 0
for i in ["a", "e", "i", "o", "u"]:
    for j in S:
        if j == i:
            count += 1
print(count)