for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = max(a)
    t1 = min(a)
    print(t - t1)
