steps = {1: 1, 2: 2}

def climb_stairs(n):
    """
    At each step can only take 1 or 2 steps
    Determine all possible ways to climb n stairs
    """
    if n in steps: return steps[n]
    else:
        steps[n] = climb_stairs(n-1) + climb_stairs(n-2)
        return steps[n]


def main():
    print(climb_stairs(4))

if __name__ == "__main__":
    main()