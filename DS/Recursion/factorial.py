# 4! = 4 * 3! = 4 * 3 * 2!..

# factorial(4) = 24
# return 4 * 6 = 24
# return 3 * 2 = 6
# return 2 * 1 = 2
# return 1
# return 4 * factorial(4-1)
# return 3 * factorial(3-1)
# return 2 * factorial(2-1)
# return 1 - base case
# 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))