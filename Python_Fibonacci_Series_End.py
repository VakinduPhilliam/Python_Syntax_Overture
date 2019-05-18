# Python Fibonacci series:
# the sum of preceding two elements defines the next.
# All Fibonacci numbers less than 1000.

a, b = 0, 1

while a < 1000:
       print(a, end=',')
       a, b = b, a+b
