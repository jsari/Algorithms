
def construct_lps(s):

    length = len(s)
    lps = [0]*length

    i, j = 1, 0

    while i <= length - 1:

        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp(s, p):

    ans = []
    aux = construct_lps(p)

    i = 0  # index for string s
    j = 0  # index for pattern p
    while i < len(s):

        if s[i] == p[j]:
            i += 1
            j += 1

            if j == len(p):
                ans.append(i - j)
                j = aux[j - 1]
        else:

            if j != 0:
                j = aux[j-1]
            else:
                i += 1

    return ans


if __name__ == "__main__":
    print(kmp("ABABDABACDABABCABAB", "ABABCABAB"))
