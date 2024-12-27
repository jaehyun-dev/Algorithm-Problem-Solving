d = {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}
l = input().split()
ans = chr(ord(l[0][0]) - 32)
for i in l[1:]:
    if i not in d:
        ans += chr(ord(i[0]) - 32)
print(ans)