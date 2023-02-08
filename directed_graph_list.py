import pprint
class Solution:

    def __init__(self):
        self.helper = {}

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        
        for edge in B:
            x, y = edge
            if x in self.helper: self.helper[x].append(y)
            else: self.helper[x] = [y]
        
        #pprint.pprint(self.helper)
        for node in self.helper:
            x = self.dfs(node, node, [])
            if x == 1: return 1
        return 0

    def dfs(self, node, target, visited):
        # if target is in children -> there is a path back
        children = self.helper.get(node, [])
        if target in children: return 1
        if len(children) == 0: return 0
        
        visited.append(node)
        
        for c in children:
            if c in visited: continue
            resp = self.dfs(c, target, visited)
            if resp == 1: return 1

        return 0

if __name__ == "__main__":
    # B = [[1, 2], 
    #     [4, 1], 
    #     [2, 4],
    #     [3, 4],
    #     [5, 2],
    #     [1, 3]]
    # A = 5

    # ------------
    # A = 5
    # B = [  [1, 2],
    #     [2, 3] ,
    #     [3, 4] ,
    #     [4, 5] ]

    # -----------
    A = 3
    B = [[1, 2],
        [1, 3],
        [2, 3]]
    
    # -----------
    # A = 3
    # B = [[1,2],
    #     [1,3],
    #     [2,3]]

#     A = 5
#     B = [
#   [1, 2],
#   [1, 3],
#   [2, 3],
#   [1, 4],
#   [4, 3],
#   [4, 5],
#   [3, 5]
#     ]
    x = Solution().solve(A, B)
    print(f"result: {x}")
