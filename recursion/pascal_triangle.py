def pascal_triangle(r, c):
    """
    Calculate the value of the pascal triangle at a point using recursion
    """
    if (c == 0) or (r == c):
        return 1

    return pascal_triangle(r-1, c-1) + pascal_triangle(r-1, c)


def main():
    print(pascal_triangle(4,2))


if __name__ == "__main__":
    main()