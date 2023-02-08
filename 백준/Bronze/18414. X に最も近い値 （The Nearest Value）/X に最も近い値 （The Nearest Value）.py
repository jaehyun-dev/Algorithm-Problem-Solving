X, L, R = map(int, input().split())
if X <= L:
    print(L)
elif R <= X:
    print(R)
else:
    print(X)