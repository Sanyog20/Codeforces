n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_even = 0
a_odd = 0
b_even = 0
b_odd = 0
for i in a:
    if i % 2 == 0:
        a_even += 1
    else:
        a_odd += 1
for i in b:
    if i % 2 == 0:
        b_even += 1
    else:
        b_odd += 1
ans = min(a_even, b_odd) + min(a_odd, b_even)
print(ans)