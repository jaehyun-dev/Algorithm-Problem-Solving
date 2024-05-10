n = int(input())
a = bin(n)[2:][::-1]
for i in range(len(a)):
    if a[i] == '1':
        print(i, end = " ")