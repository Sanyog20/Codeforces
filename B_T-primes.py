def solve(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 3:
        return True
    return False

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if solve(a[i]):
        print("YES")
    else:
        print("NO")