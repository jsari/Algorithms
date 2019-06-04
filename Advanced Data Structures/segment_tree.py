
# A segment tree is a tree data structure used for storing information about intervals.
# It allows querying which of the stored segments contain a given point.
#
# It supports two operations
# a) range query: O(logn)
# b) update an item: O(logn)


class SegmentTree:

    # data: the segment tree
    # length: the length of the original array
    #
    # operation: the function to compute the range queries
    #
    # Examples
    # min: for minimum range queries ( init_value = math.inf )
    # max: for maximum range queries ( init_value = -math.inf )
    # operator.add: for sum range queries ( init_value = 0 )

    def __init__(self, arr, operation, init_value):
        self.data = [0] * 2 * len(arr)
        self.length = len(arr)
        self.operation = operation
        self.init_value = init_value
        self.construct(arr)

    # Construct a segment tree of length 2*n where the values of the original array
    # stored to the second half of the array
    def construct(self, arr):
        self.data[self.length:] = arr
        for index in reversed(range(self.length)):
            self.data[index] = self.operation(self.data[2 * index], self.data[2 * index + 1])

    # update the original array and segment tree
    def update(self, index, value):
        index += self.length
        self.data[index] = value

        while index > 1:
            index //= 2
            self.data[index] = self.operation(self.data[2 * index], self.data[2 * index + 1])

    # Compute the query in range [left, right)
    def query(self, left, right):

        left += self.length
        right += self.length
        result = self.init_value

        while left < right:

            if left % 2 == 1:
                result = self.operation(result, self.data[left])
                left += 1

            if right % 2 == 1:
                right -= 1
                result = self.operation(result, self.data[right])

            left //= 2
            right //= 2

        return result


def main():
    import operator
    array = [10, 14, 4, 8, 9, 12, 4, 7, 4, 2, 17]
    st = SegmentTree(array, operator.add, 0)

    print("Construct segment tree...")
    print(st.data)
    print("Min range query(4, 5)", st.query(4, 5))
    st.update(6, 14)
    print("Min range query(2, 8)", st.query(2, 11))


if __name__ == "__main__":
    main()
