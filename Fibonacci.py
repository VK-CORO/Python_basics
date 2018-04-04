def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
n=100
a,b = 0,1
while a < n:
    	print(a)
    	a, b = b, a+b
while b < n:
	print(b)