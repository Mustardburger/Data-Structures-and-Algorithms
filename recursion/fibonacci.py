memoization = {0: 0, 1: 1}

def fibo(n):
    """
    Return the nth number of the Fibonacci sequence
    """
    if n in memoization: return memoization[n]
    return 