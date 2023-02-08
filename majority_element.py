class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        tracker = {}
        for x in A:
            if x in tracker: tracker[x] += 1
            else: tracker[x] = 1
            
        tracker = dict(sorted(tracker.items(), key=lambda item: item[1],reverse=True))
        return list(tracker.keys())[0]
        

if __name__ == "__main__":
    Solution().majorityElement([1,2,1])