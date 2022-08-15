# iterative
def Factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        print(i, "! =", result)
    return result


# print(Factorial(7))

# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1)*n


print(factorial(4))
