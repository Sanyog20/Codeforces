n, k = map(int, input().split())
if n % 10 == k:
    ans = 1
    print(ans)
else:
    ans = 0
    n1 = n % 10
    while(n1 != k):
        ans = ans + 1
        n1 = (n * ans) % 10
        if n1 % 10 == 0:
            ans = ans
            break
    print(ans)