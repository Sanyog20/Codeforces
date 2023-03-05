for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for j in a:
        if j % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    if even == odd:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)