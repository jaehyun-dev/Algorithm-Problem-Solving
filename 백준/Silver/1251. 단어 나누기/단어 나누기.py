a = input()
precedence = 'z' * len(a)
for i in range(1, len(a) - 1):
    for j in range(i + 1, len(a)):
        l = a[:i][::-1]
        m = a[i:j][::-1]
        n = a[j:len(a)][::-1]
        word = l + m + n
        for k in range(len(a)):
            if ord(precedence[k]) > ord(word[k]):
                precedence = word
                break
            elif ord(precedence[k]) < ord(word[k]):
                break
print(precedence)