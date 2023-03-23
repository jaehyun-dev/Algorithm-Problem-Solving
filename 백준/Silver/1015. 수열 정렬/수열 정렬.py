N = int(input())
A = list(map(int, input().split()))
s = sorted(set(A))
count_dic = {}
P = [0] * N
for i in s:
    count_dic[i] = A.count(i)
j = 0
for i in s:
    count = 0
    element_index = 0
    while count < count_dic[i]:
        P_index = A.index(i, element_index)
        P[P_index] = j
        element_index = P_index + 1
        count += 1
        j += 1

print(" ".join(map(str, P)))