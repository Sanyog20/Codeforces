for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t1 = min(a)
    t2 = min(b)
    moves = 0
    for i in range(n):
        a1 = a[i] - t1
        b1 = b[i] - t2
        moves = moves + max(a1, b1)
    print(moves)