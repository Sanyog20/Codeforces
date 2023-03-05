n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(int(n / 2)):
    ans = ans + ((a[i] + a[-i - 1]) ** 2)
print(ans)
