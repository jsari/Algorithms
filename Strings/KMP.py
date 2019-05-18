
# Knuth Morris Pratt Algorithm
# -----------------------------
# The KMP algorithm searches for all occurrences of a string P within a string S
#
# Definitions:
# -----------------------------
# Border of a string is a prefix of the string
# which is equal to the suffix of the string of the same length.
#
# Prefix function of a string P is a function s(i) that
# for each i returns the length of the longest border of the prefix P[:i]
#
#
# Time Complexity of Knuth Morris Pratt algorithm
# -----------------------------
# Algorithm : O(|p| + |s|)
# Function compute_prefix_function : O(|p|)
#


def compute_prefix_function(p):

    length = len(p)
    lps = [0]*length

    border = 0
    for i in range(1, length):

        while border > 0 and p[i] != p[border]:
            border = lps[border - 1]

        if p[i] == p[border]:
            border += 1
        else:
            border = 0

        lps[i] = border

    return lps


def kmp(t, p):

    prefix_function = compute_prefix_function(p + "$" + t)

    result = []
    for index, value in enumerate(prefix_function[len(p):]):
        if value == len(p):
            result.append(index - len(p))

    return result


if __name__ == "__main__":
    print(kmp("ABABDABACDABABCABAB", "ABABCABAB"))
