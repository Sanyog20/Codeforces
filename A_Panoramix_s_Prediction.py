def isPrime(t):
    if t % 2 == 0:
        return False
    
    else:
        for i in range(3, int(t ** 0.5) + 1, 2):
            if t % i == 0:
                return False
        else:
            return True

def solve(n, k):
    if isPrime(k):
        for i in range(n + 1, k):
            if isPrime(i):
                return False
        else:
            return True
    else:
        return False

n , k = map(int, input().split())
t = solve(n, k)
if t == True:
    print("YES")
else:
    print("NO")
