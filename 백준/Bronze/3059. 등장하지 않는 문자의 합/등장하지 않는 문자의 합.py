T = int(input())
for _ in range(T):
    S = input()
    char_set = set(S)
    count = 0
    for i in range(65, 91):
        if chr(i) not in char_set:
            count += i
    print(count)