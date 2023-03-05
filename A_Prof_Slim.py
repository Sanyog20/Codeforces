for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    negative = 0
    for i in a:
        if i < 0:
            negative += 1
    b = []
    for i in a:
        if negative > 0:
            b.append(-1 * (abs(i)))
            negative -= 1
        else:
            b.append(abs(i))
    a = b.copy()
    a.sort()
    if a == b:
        print("YES")
    else:
        print("NO")
