for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(n - 1):
        b.append(a[i + 1] - a[i])
    print(min(b))
