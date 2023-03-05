for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    if total % n == 0:
        print(0)
    else:
        print(1)