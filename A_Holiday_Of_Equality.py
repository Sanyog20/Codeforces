n = int(input())
a = list(map(int, input().split()))
ans = (max(a) * n) - sum(a)
print(ans)