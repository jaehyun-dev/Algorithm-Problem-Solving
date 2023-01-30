a = input().split()
b = input().split()
start = int(a[0]) * 3600 + int(a[2]) * 60 + int(a[4])
end = int(b[0]) * 3600 + int(b[2]) * 60 + int(b[4])
second = end - start
print(second if second > 0 else second + 86400)