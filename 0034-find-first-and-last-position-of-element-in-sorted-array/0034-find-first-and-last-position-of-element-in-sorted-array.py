class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
       
        j=0
        for i in range(len(nums)):
            if nums[i]==target:
                if j==0:
                    res[0]=i
                    j+=1
                res[1]=i
        return res            
        