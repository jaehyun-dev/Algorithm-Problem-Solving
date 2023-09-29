a = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna stop"""
N = int(input())
flag = True
for _ in range(N):
    if input() not in a:
        flag = False
        break
print("No" if flag else "Yes")