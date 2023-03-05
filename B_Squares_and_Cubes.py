for _ in range(int(input())):
    n = int(input())
    t = []
    for i in range(1, int(n ** 0.5) + 1):
        t1 = i * i
        t2 = i * i * i
        if t1 <= n:
            t.append(t1)
        if t2 <= n:
            t.append(t2)
    t = set(t)
    print(len(t))
