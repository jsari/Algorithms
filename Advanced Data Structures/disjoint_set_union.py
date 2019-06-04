
# A disjoint-set-union is a data structure that tracks a set of elements
# partitioned into a number of disjoint (non-overlapping) subsets.
#
# It supports two operations:
#
#   1) Union(A, B): Combine two subsets into a single subset.
#   2) Find(A, B): Find whether two elements are in the same subset.
#
from collections import defaultdict


class DisjointSet:

    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    # Find the root of an element (with data compression)
    def root(self, i):

        while self.arr[i] != i:
            self.arr[i] = self.arr[self.arr[i]]
            i = self.arr[i]
        return i

    # Combine two groups based on their size
    def weighted_union(self, a, b):

        root_a, root_b = self.root(a), self.root(b)
        if root_a != root_b:
            if self.size[root_a] < self.size[root_b]:
                self.arr[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            else:
                self.arr[root_b] = root_a
                self.size[root_a] += self.size[root_b]

    # Check if elements a and b are connected
    def find(self, a, b):
        return self.root(a) == self.root(b)

    # Return all disjoint sets
    def get_subsets(self):

        subsets = defaultdict(set)

        for i, x in enumerate(self.arr):
            subsets[self.root(i)].add(i)

        return subsets.values()

    # Return the total number of disjoint sets
    def count_subsets(self):
        total = 0
        for x in self.arr:
            if x == self.arr[x]:
                total += 1

        return total


def main():

    pass


if __name__ == "__main__":
    main()
