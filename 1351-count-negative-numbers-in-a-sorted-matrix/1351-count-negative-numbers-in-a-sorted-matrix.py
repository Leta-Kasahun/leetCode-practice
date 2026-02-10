class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        negative=0
        for i in grid:
            for j in i:
                if j<0:
                    negative+=1
        return negative            
