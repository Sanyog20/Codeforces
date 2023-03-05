n = int(input())
a = list(map(int, input().split()))
sereja = 0
dima = 0
i = -1
j = 0
count = 0
while n:
    count = count + 1
    t1 = a[j]
    t2 = a[i]
    if t2 > t1:
        i = i - 1
    