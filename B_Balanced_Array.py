for _ in range(int(input())):
    n = int(input())
    if n % 4 != 0:
        print("NO")
    else:
        a = []
        b = []
        for i in range(1, int(n / 2) + 1):
            a.append(i * 2)
        for i in range(int(n / 2) - 1):
            b.append((i * 2) + 1)
        b.append(sum(a) - sum(b))
        print("YES")
        print(*a, *b)