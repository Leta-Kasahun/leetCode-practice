class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        for i in nums:
            if i in seen:
                return i
                break
            seen[i]=True    


