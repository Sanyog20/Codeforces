n, m = map(int, input().split())
a = list(map(int, input().split()))
time = a[0] - 1
for i in range(1, m):
    if a[i] < a[i - 1]:
        time = time + (n - a[i - 1] + a[i])
    else:
        time = time + a[i] - a[i - 1]
print(time)