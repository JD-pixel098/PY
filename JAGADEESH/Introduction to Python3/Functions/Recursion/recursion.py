def factorial(n):
    if n <= 1:
        return 1
    else:
        # calculate n multiplied by the factorial of n - 1
        return (n * factorial(n-1))


num = 3
print("The factorial of", num, "is", factorial(num))


print(factorial(12))
