n = int(input())
ans = 0
for i in range(0, n):
    ans = ans + (i * (n - i))
print(ans + n)
