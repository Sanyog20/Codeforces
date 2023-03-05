a = list(map(int, input().split()))
counter = 0
for i in a:
    if i == 0:
        a.remove(i)
        a.append(0)
print(*a)