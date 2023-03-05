a = int(input())
b = int(input())
n = a + b + 1
l = []
c = n - a
while(c <= n):
    l.append(c)
    c = c + 1
c = b
while(c >= 1):
    l.append(c)
    c = c - 1
print(*l)