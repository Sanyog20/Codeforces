for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count = count + 1
    a.sort()
    a[-1] = a[-1] * (2 ** count)
    print(int(sum(a)))