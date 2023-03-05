for _ in range(int(input())):
    n = int(input())
    r = n // 10
    if n % 7 == 0:
        print(n)
    else:
        n = (r * 10) + 1
        if n % 7 == 0:
            print(n)
        else:
            while n % 7 != 0:
                n = n + 1
            print(n)