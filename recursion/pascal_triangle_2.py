def get_row(ind):
    """
    From the index of the row, return all the values
    of that row of the Pascal Triangle
    """
    if ind == 0:
        return [1]
    if ind == 1:
        return [1, 1]

    row = []
    row_above = get_row(ind-1)
    for i in range(len(row_above)+1):
        if i == 0 or i == len(row_above):
            row.append(1)
        else:
            row.append(row_above[i-1] + row_above[i])

    return row


def main():
    print(get_row(3))

if __name__ == "__main__":
    main()