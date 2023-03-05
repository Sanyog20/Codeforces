for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    t = max(p)
    t1 = p.index(t)
    if t1 != n - 1 and t1 != 0:
        a = [-1]
    elif t1 == 0:
        a = p[1:]
        a = a[::-1]
        a.insert(0, t)
    else:
        temp = p[:n - 1]
        a = temp[::-1]
        a.insert(0, t)
    print(*a)