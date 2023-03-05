for i in range(int(input())):
    k = int(input())
    count = 0
    i = 1
    while True:
        t = str(i)
        if i % 3 != 0 and t[-1] != '3':
            count += 1
        if count == k:
            print(i)
            break
        i += 1