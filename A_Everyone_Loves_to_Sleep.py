for _ in range(int(input())):
    n, H, M = map(int, input().split())
    ans = 999999
    const = (H * 60) + M
    for i in range(n):
        hi, mi = map(int, input().split())
        t = hi * 60 + mi
        if t < const:
            t1 = (24 - H) * 60 - M
            t2 = hi * 60 + mi
            t = t1 + t2
            ans = min(ans, t)
        else:
            t = (hi * 60) + mi
            ans = min(ans, abs(t - const))
    print(ans // 60, ans % 60)
