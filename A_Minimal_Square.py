for _ in range(int(input())):
    a, b = map(int, input().split())
    t = min(a, b)
    if a == b:
        print(a * a * 4)
    elif (2 * t) >= b and (2 * t) >= a:
        print(t * t * 4)
    else:
        print(max(a, b) * max(a, b))