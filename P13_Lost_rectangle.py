n = int(input())
if int(n ** 0.5) == n ** 0.5:
    side1 = int(n ** 0.5)
    side2 = int(n ** 0.5)
else:
    side1 = int(n ** 0.5)
    side2 = int(n ** 0.5) + 1
    while(side1 * side2 != n):
        side1 -= 1
        side2 += 1
print(2 * (side1 + side2))