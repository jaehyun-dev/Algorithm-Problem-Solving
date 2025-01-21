N = int(input())
f = input()
d = input()
fi = int(f, 2)
di = int(d, 2)
print("Deletion ", end="")
if (N % 2 and fi ^ di == (1 << len(f)) - 1) or (not N % 2 and f == d):
    print("succeeded")
else:
    print("failed")