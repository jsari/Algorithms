
# LCS problem :
# Given two sequences, find the length of longest subsequence present in both of them.
#
# Time Complexity : O(m*n)


def lcs(str1: str, str2: str, backtrack: bool = False):

    sub_seq = []

    # Get the length of the two strings
    m = len(str1)
    n = len(str2)

    # Construct the initial array
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Compute each value iteratively
    for row in range(1, m+1):
        for col in range(1, n+1):

            if str1[row-1] == str2[col-1]:
                dp[row][col] = 1 + dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])

    # Find one longest common subsequence
    if backtrack:
        row, col = m, n
        while row > 0 and col > 0:
            if str1[row-1] == str2[col-1]:
                sub_seq.append(str1[row-1])
                row -= 1
                col -= 1
            elif dp[row][col-1] >= dp[row-1][col]:
                col -= 1
            else:
                row -= 1

    return dp[m][n], ''.join(reversed(sub_seq))


def main():
    f_string = input("Give the first string: ")
    s_string = input("Give the second string: ")
    length, subsequence = lcs(f_string, s_string, backtrack=True)
    print("The length of the longest common subsequence is:", length)
    print("A longest common subsequence is:", subsequence)


if __name__ == "__main__":
    main()
