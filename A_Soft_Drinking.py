n, k, l, c, d, p, nl, np = map(int, input().split())
drink = (l * k) / (nl)
slice = (c * d)
salt = p / np
print(int(min(drink, slice, salt) / n))