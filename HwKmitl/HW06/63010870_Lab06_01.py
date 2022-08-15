def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


inp = int(input("Enter Number : "))
fibo = fibonacci(inp)
print(f"fibo({inp}) = {fibo}")
