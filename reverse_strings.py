class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        items = A.split(" ")
        items.reverse()
        items = [x for x in items if x != ""]
        
        return " ".join(items)

if __name__ == "__main__":
    print(Solution().solve(" the sky is blue "))