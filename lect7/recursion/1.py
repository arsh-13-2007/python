# power of number 
# binary serach 
# multiplication of 2 number 
# fibinacci series
# sum of digits
# 1. fibinacci series 
def fibonacci(n):
   
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n):
    
    for i in range(n):
        print(fibonacci(i), end=' ')


n_terms = 10
print(f"Fibonacci series up to {n_terms} terms:")
print_fibonacci_series(n_terms)
