class Solution:

    def __init__(self):
        ...

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        
        # init matrix 
        self.matrix = [[0 for _ in range(A+1)] for _ in range(A+1)] 

        # set edges
        for edge in B:
            x, y = edge
            self.matrix[x][y] = 1

        """  0  1  2  3  4  5
        0 [ [0, 0, 0, 0, 0, 0], 
        1   [0, 0, 1, 1, 0, 0], 
        2   [0, 0, 0, 0, 1, 0], 
        3   [0, 0, 0, 0, 1, 0], 
        4   [0, 1, 0, 0, 0, 0], 
        5   [0, 0, 1, 0, 0, 0] ]

        """
        return self.dfs(0, [])
        
    def dfs(self,x , visited):
        for x in range(x, len(self.matrix)):
            for y in range(0, len(self.matrix)):
                
                if self.matrix[x][y] == 0:  continue
                if x == y: return 1

                print(f"analyzing: {x} -> {y}")
                if y in visited:
                    print(f"cycle detected")
                    return 1

                # add source node as visited
                print(f"adding to visited: {x}")
                visited.append(x)
                print(f"x: {x}")

                children = [idx for idx, a in enumerate(self.matrix[x]) if a == 1]
                print(f"{x} children: {children}")
                for c in children:
                    return self.dfs(c, visited)

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
    A = 5
    B = [  [1, 2],
        [2, 3] ,
        [3, 4] ,
        [4, 5] ]

    # -----------
    A = 3
    B = [[1, 3],
        [2, 3],
        [3, 2]]
    x = Solution().solve(A, B)
    print(f"result: {x}")
