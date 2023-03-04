S = input()
count = 1
i = 1
while i < len(S):
    if S[i] != S[i - 1]:
        count += 1
    i += 1
print(count // 2)