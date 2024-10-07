h = int(input())
m = int(input())
hl = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "one"]
ml = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
hd = [None, "ten", "twenty", "thirty", "forty", "fifty"]
hour = hl[h]
minute = ""
ans = ""
if m == 0:
    ans = f"{hour} o' clock"
elif m <= 30:
    if m <= 20:
        minute = ml[m]
    elif m < 30:
        minute = hd[m // 10] + " " + ml[m % 10]
    minute += " minute"
    if 1 < m and m % 15 != 0:
        minute += "s"
    if m == 15:
        minute = "quarter"
    elif m == 30:
        minute = "half"
    ans = f"{minute} past {hour}"
else:
    hour = hl[h + 1]
    m = 60 - m
    if m <= 20:
        minute = ml[m]
    else:
        minute = hd[m // 10] + " " + ml[m % 10]
    minute += " minute"
    if 1 < m:
        minute += "s"
    if m == 15:
        minute = "quarter"
    elif m == 30:
        minute = "half"
    ans = f"{minute} to {hour}"
print(ans)