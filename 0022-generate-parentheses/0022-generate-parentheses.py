class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        def backtrack(left,right,current):
            if left>n or right>n or left<right:
                return False
            if left==n and right==n:
                result.append(current)
            backtrack(left+1,right,current+'(')
            backtrack(left,right+1,current+')')
        backtrack(0,0,'')
        return result         