def compare(x1, x2):
    if x1 > x2:
        print(">")
    elif x1 == x2:
        print("=")
    else:
        print("<")


for _ in range(int(input())):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    x1 = (10 ** p1) * x1
    x2 = (10 ** p2) * x2
    compare(x1, x2)
