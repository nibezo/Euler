def fibonacci(n):
    if n in range(1, 3):
        return n
    return fibonacci(n-1) + fibonacci(n - 2)


x = 0  # the value of all fibonacci numbers to four million
n = 1  # counter for cycle
sum_fib = 0  # sum of all even fibonacci numbers to four million

while x < 4000000:
    x = fibonacci(n)
    if x % 2 == 0:
        sum_fib += x
    n = n + 1

print(sum_fib, "is the sum of all even Fibonacci\
 numbers to 4 million")
# https://projecteuler.net/problem=2 => problem description
