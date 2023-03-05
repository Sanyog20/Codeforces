for i in range(int(input())):
    l, r = map(int, input().split())
    if l <= r // 2:
        print(r % ((r // 2) + 1))
    else:
        print(r % l)