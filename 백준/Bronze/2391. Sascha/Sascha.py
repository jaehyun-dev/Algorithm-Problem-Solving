n = int(input())
for _ in range(n):
    word = input()
    w = int(input())
    d = len(word) + 1
    for i in range(w):
        c = 0
        dic = input()
        for j in range(len(dic)):
            if word[j] != dic[j]:
                c += 1
        if c < d:
            d = c
            ans = dic
    print(ans)