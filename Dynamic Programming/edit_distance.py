
# The edit distance is the minimum number of operations (insert, delete, modify)
# needed to transform a string into another string.
#
# The following code implements Wagner–Fischer algorithm
#
# Time Complexity : O(n*m)


def edit_distance(s: str, t: str):

    n = len(s)
    m = len(t)

    # initialize a matrix that will hold all distances
    # between all prefixes of s with all prefixes of t
    dist = [[0]*(m+1) for _ in range(n+1)]
    dist[0] = [i for i in range(m+1)]
    for row in range(n):
        dist[row][0] = row

    # calculate all distances iteratively
    for row in range(1, n+1):
        for col in range(1, m+1):
            if s[row-1] == t[col-1]:
                dist[row][col] = dist[row-1][col-1]
            else:
                dist[row][col] = min(dist[row-1][col] + 1,
                                     dist[row][col-1] + 1,
                                     dist[row-1][col-1] + 1)

    return dist[n][m]


def main():
    f_string = input("Give the first string: ")
    s_string = input("Give the second string: ")
    print("The Levenshtein distance of strings is:", edit_distance(f_string, s_string))


if __name__ == "__main__":
    main()
