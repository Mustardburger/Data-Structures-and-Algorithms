def reverse_string(l):
    """
    l is a list of char. Reverse this list using recursion
    """
    if len(l) == 0:
        return []
    return [l[-1]] + reverse_string(l[:-1])

def main():
    l = ["H", "e", "l", "l", "o"]
    l = reverse_string(l)
    print(l)


if __name__ == "__main__":
    main()