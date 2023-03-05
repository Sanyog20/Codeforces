for i in range(int(input())):
    x, n = map(int, input().split())
    for j in range(1, n + 1):
        if x % 2 == 0:
            x = x - j
        else:
            x = x + j
    print(x)