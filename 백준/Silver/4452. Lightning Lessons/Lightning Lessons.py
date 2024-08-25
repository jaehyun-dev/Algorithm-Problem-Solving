N = int(input())
for _ in range(N):
    l = list(map(int, input().split()))
    M, A = l[0], l[1:]
    cnt = 0
    while set(A) != {0} and 1 < len(A):
        temp = []
        for i in range(len(A) - 1):
            temp.append(A[i + 1] - A[i])
        A = temp
        cnt += 1
    if not sum(A):
        print("z" * cnt + "ap!")
    elif 0 < A[0]:
        print("*fizzle*")
    else:
        print("*bunny*")