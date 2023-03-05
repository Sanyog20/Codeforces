for i in range(int(input())):
    s = list(input())
    t = list(input())
    count = 0
    for j in range(1, len(t)):
        t1 = abs(s.index(t[j]) - s.index(t[j - 1]))
        count = count + t1
    print(count)