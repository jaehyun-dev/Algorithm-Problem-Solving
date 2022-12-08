n = list(input())
for i in range(len(n)):
    if n[i].isupper():
        n[i] = n[i].lower()
    else:
        n[i] = n[i].upper()
    print(n[i], end="")