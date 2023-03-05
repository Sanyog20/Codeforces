for _ in range(int(input())):
    n = input()
    a = []
    for i in range(len(n)):
        if n[i] != '0':
            a.append(n[i] + ('0' * (len(n) - i - 1)))
    print(len(a))
    print(*a)
