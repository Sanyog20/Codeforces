n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
t = n
for i in range(n):
    if a[i] > (5 - k):
        t = i
        break
print(int(t / 3))
