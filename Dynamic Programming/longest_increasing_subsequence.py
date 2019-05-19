
# LIS problem :
# Find the length of the longest subsequence of a given sequence
# such that all elements of the subsequence are sorted in increasing order.
#
# Time Complexity : O(n*logn)
from bisect import bisect_left


def lis(arr: list):

    n = len(arr)
    sub_seqs = [0] * (n + 1)
    sub_seqs[0] = arr[0]
    pos = 1

    for i in range(1, n):
        if arr[i] < sub_seqs[0]:
            sub_seqs[0] = arr[i]
        elif arr[i] > sub_seqs[pos - 1]:
            sub_seqs[pos] = arr[i]
            pos += 1
        else:
            new_pos = bisect_left(sub_seqs[:pos], arr[i])
            sub_seqs[new_pos] = arr[i]

    return pos


def main():
    seq = input("Give me a sequence of numbers: ").split()
    print("Longest increasing subsequence:", lis(seq))


if __name__ == "__main__":
    main()
