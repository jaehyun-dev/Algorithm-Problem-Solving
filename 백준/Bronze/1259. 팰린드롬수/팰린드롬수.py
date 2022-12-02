import sys

def is_palindrome(n):
    for i in range((len(n) // 2)):
        if n[i] != n[len(n) - 1 - i]:
            return "no"
    return "yes"

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(is_palindrome(str(line.strip())))