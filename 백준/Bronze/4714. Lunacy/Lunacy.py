while True:
    a = float(input())
    if a == -1.0:
        break
    print(f"Objects weighing {format(a, '.2f')} on Earth will weigh {format(a * 0.167, '.2f')} on the moon.")