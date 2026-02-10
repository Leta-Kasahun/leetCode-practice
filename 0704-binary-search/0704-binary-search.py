class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right=len(nums)-1
        left=0
        index=-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return index                
        