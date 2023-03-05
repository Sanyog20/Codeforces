n = int(input())
a = list(map(int, input().split()))
odd = 0
even = 0
for i in range(n):
    if a[i] % 2 == 0:
        even = even + 1
        lastEven = i + 1
    else:
        odd = odd + 1
        lastOdd = i + 1
    if even > 1 and odd == 1:
        print(lastOdd)
        break
    elif  odd > 1 and even == 1:
        print(lastEven)
        break