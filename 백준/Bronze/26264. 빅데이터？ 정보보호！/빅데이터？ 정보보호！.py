N = int(input())
s = input()
sc = s.count("security")
bc = s.count("bigdata")
if sc < bc:
    print("bigdata?")
elif bc < sc:
    print("security!")
else:
    print('bigdata? security!')