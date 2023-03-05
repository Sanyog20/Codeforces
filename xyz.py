# Function to check if a given number is prime or not
def isPrime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        for i in range(n):
            if n % i == 0:
                return False
        return True

# Function to count the number of students having greater than or equal marks as the kth student
def countStudents(arr, k):
    count = 0
    for i in range(len(arr)):
        if arr[i] >= arr[k]:
            count = count + 1
    return count

# Taking input from user
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Checking wheter the no of students satisfying the given condition is prime or not and printing accprdingly
if isPrime(countStudents(arr, k)):
    print("Eligible")
else:
    print("Non Eligible")
