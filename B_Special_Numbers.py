for i in range(int(input())):
    n, k = map(int, input().split())
    a = bin(k).replace("0b", "")
    t = len(a)
    ans = 0
    for j in range(t):
        if a[j] == '1':
            ans = ans + n ** (t - j - 1)
    print(ans % 1000000007)