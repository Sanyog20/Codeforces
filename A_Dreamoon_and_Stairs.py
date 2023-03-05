n, m = map(int, input().split())
if m > n:
    print(-1)
elif n % 2 == 0:
    t = n // 2
    t1 = t % m
    if t1 == 0:
        print(t1)
    else:
        print(t + t1)
else:
    t = (n // 2) + 1
    t1 = t % m
    if t1 == 0:
        print(t1)
    else:
        print(t + t1)
