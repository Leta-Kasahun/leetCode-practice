class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        filtered=set(nums) 
        if len(nums)==len(filtered):
            return False
        else:
            return True 

