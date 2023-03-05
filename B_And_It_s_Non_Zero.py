for i in range(int(input())):
    l, r = map(int, input().split())
    t = bin(l).replace("0b", "")
    t = t[::-1]
    t1 = t.index('1')
    count = 0
    for j in range(l, r + 1):
        temp = bin(j).replace("0b", "")
        temp = temp[::-1]
        if temp[t1] == '0':
            count += 1
    print(count)
