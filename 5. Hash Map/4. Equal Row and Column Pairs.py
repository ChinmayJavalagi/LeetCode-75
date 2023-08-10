'''
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
'''

class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        c = 0
        dic = defaultdict(int)
        for row in grid:
            r = str(row)
            dic[r]+=1
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            c+=dic[str(col)]
        return c
