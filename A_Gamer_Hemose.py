for i in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    h = h - a[-1]
    count = 1
    if h > 0:
        h = h - a[-2]
        count += 1
        if h > 0:
            t = a[-1] + a[-2]
            count = count + 2 *(h // t)
            h = h % t
            if h > 0:
                h = h - a[-1]
                count += 1
                if h > 0:
                    count += 1
    print(count)
