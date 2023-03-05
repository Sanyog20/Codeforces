for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = 0
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            flag = 1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
