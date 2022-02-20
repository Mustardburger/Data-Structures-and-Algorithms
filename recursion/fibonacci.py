memoization = {0: 0, 1: 1}

def fibo(n):
    """
    Return the nth number of the Fibonacci sequence
    """
    if n in memoization: return memoization[n]
    else: 
        a = fibo(n-1)
        b = fibo(n-2)
        memoization[n] = a + b
        return memoization[n]


def main():
    print(fibo(7))

if __name__ == "__main__":
    main()