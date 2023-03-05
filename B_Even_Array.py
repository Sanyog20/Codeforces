for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            if a[i] % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
    if even == odd:
        print(even)
    else:
        print(-1)