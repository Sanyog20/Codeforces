for _ in range(int(input())):
    x, y, n = map(int, input().split())
    if y == 0:
        if x > n:
            print(0)
        else:
            t = (n // x) * x
            if t + y <= n:
                print(t + y)
            else:
                print(t - x + y)
    elif n % x == 0:
        print(max(0, n - x + y))
    else:
        t = (n // x) * x
        if t + y <= n:
            print(t + y)
        else:
            print(t - x + y)