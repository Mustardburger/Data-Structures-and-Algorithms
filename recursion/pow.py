def power(x, n):
    """
    Take x to the power of n (x^n)
    """
    if n == 0: return 1.0
    def recursion(n):
        if n > 0:
            if n == 1: return x
            else: return x*recursion(n-1)
        if n < 0:
            if n == -1: return 1/x
            else: return (1/x)*recursion(n+1)

    return recursion(n)

def main():
    print(power(2.0, -2))

if __name__ == "__main__":
    main()