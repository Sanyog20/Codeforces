n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    print(max(a[0], l - a[0]))
else:
    max_diff = a[1] - a[0]
    for i in range(1, n):
        t = a[i] - a[i - 1]
        if t > max_diff:
            max_diff = t
    if (a[0] == max_diff or max_diff / 2 < a[0]) and (a[0] > (l - a[-1])):
        print(a[0])
    elif (l - a[-1]) == max_diff or max_diff / 2 < (l - a[-1]):
        print(l - a[-1])
    else:
        print(max_diff / 2)
