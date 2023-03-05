n = int(input())
a = list(map(int, input().split()))
count = 0
m1 = a[0]
m2 = a[0]
for i in range(1, n):
    if a[i] < m1 or a[i] > m2:
        m1 = min(a[i], m1)
        m2 = max(a[i], m2)
        count = count + 1
print(count)