import operator
a, b, c = map(int, input().split())
oper = [operator.add, operator.sub, operator.mul, operator.truediv]
oper_str = ["+", "-", "*", "/"]
for i in range(4):
    if oper[i](a, b) == c:
        print(f"{a}{oper_str[i]}{b}={c}")
    elif a == oper[i](b, c):
        print(f"{a}={b}{oper_str[i]}{c}")