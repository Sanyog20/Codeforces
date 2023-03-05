import math


for _ in range(int(input())):
    hc, dc = map(int, input().split())
    hm, dm = map(int, input().split())
    k, w, a = map(int, input().split())
    for i in range(k + 1):
        c = math.ceil((hc + ((k - i) * a)) / dm)
        m = math.ceil(hm / (dc + (i * w)))
        if c >= m:
            print("YES")
            break
    else:
        print("NO")
