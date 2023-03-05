from time import time


n, k = map(int, input().split())
time_remaining = 240 - k
count = 0
while(True):
    if time_remaining >= ((count + 1) * 5):
        time_remaining = time_remaining - ((count + 1) * 5)
        count = count + 1
    else:
        break
print(min(count, n))
