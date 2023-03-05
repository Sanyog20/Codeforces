for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    swaps = 0
    for i in range(n):
        if swaps == k:
            break
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
            swaps = swaps + 1
    print(sum(a))