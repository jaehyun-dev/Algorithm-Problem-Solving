P, K = map(int, input().split())
isprime = [True] * K
isprime[0] = False
isprime[1] = False
for i in range(2, K):
    if isprime[i]:
        j = 2
        while i * j < K:
            isprime[i * j] = False
            j += 1
flag = True
for i in range(2, K):
    if isprime[i]:
        if P % i == 0:
            print("BAD", i)
            flag = False
            break
if flag:
    print("GOOD")