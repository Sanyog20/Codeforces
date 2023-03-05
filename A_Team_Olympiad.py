n = int(input())
a = list(map(int, input().split()))
one = []
two = []
three = []
for i in range(n):
    if a[i] == 1:
        one.append(i + 1)
    elif a[i] == 2:
        two.append(i + 1)
    else:
        three.append(i + 1)
t = min(len(one), len(two), len(three))
print(t)
for i in range(t):
    print(one[i], two[i], three[i])