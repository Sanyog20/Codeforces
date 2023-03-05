n, b = map(int, input().split())
a = list(map(int, input().split()))
t = max(a)
l = []
s = 0
for i in range(n):
    t1 = t - a[i]
    l.append(t1)
    s = s + t1
if s > b:
    print(-1)
elif s == b:
    for i in range(n):
        print(format(l[i], ".6f"))
else:
    rem = b - s
    vol = rem / n
    for i in range(n):
        t = vol + l[i]
        print(format(t, ".6f"))
