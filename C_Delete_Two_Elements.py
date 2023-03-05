for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mean = sum(a) / n
    count = 0
    if len(set(a)) == 1:
        count = n * (n - 1) / 2
    else:
        for j in range(n):
            t = (2 * mean) - a[j]
            if t in a[j + 1:]:
                count += 1
    print(int(count))
