class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        add=0
        lists=[]
        for i in nums:
            add+=i
            lists.append(add)
        return lists    
