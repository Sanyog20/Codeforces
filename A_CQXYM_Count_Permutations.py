def fact(n):
    mul = 1
    for i in range(1, (2 * n) + 1):
        mul = (mul * i)
    return mul

for _ in range(int(input())):
    n = int(input())
    ans = int(fact(n) // 2) % 1000000007
    print(ans)