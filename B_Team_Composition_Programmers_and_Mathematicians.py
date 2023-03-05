for _ in range(int(input())):
    a, b = map(int, input().split())
    t = int((a + b) / 4)
    if a < t or b < t:
        print(min(a, b))
    else:
        print(t)
