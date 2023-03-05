class Math:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def ascending(self):
        sequence = self.numbers

        for i in range(1, len(sequence)):
            key = sequence[i]  # current value
            j = i - 1  # previous index

            while j >= 0 and sequence[j] > key:
                # when j is a positive number, and the previous value is greater than the current value:

                sequence[j + 1] = sequence[j]
                #        ^^^^^         ^^^^
                #      current index   previous index

                # So this means we are saying that the current index is now the previous index
                j -= 1
                # we have to decrement j to continue searching through the sequence.

            sequence[j + 1] = key
            # this inserts the value the same position as we need as
            # j is defined as  i - 1 and we are doing j + 1
            # the +1 & -1 cancel eachother so we end up inserting at the exact index
        return sequence
