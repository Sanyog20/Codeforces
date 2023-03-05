for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == l[1]:
        if l[2] % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif l[1] == l[2]:
        if l[0] % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif l[2] == l[0] + l[1]:
        print("YES")
    else:
        print("NO")