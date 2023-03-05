n = int(input())
a = list(map(int, input().split()))
count = 0
t = 0
for i in a:
    if i == -1:
        if t == 0:
            count = count + 1
        else:
            t = t - 1
    else:
        t = t + i
print(count)