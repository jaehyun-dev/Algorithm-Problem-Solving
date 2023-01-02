import datetime
for i in ["year", "month", "day"]:
    print(eval(f"datetime.date.today().{i}"))