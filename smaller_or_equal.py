class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        left = 0
        right = n - 1

        count = 0

        while (left <= right):
            mid = int((right + left) / 2)
            # Check if middle element is less than or equal to B
            if (A[mid] <= B):

                # At least (mid + 1) elements are there whose values are less than or equal to key
                count = mid + 1
                left = mid + 1

            # If B is smaller, ignore right half
            else:
                right = mid - 1

        return count


if __name__ == "__main__":
    print(Solution().solve([1, 3, 4, 4, 6, 6, 6, 6, 6, 7], 6))
