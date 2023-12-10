# Demonstration of a function to calculate the numbers in the Fibonacci sequence,
def fib(n):
    old, new = 0, 1
    for i in range(n):
        old, new = new, old + new
    return old


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))
print(fib(10))

print("FIBONACCI SEQUENCE IS LIKE A MAGIC...")
