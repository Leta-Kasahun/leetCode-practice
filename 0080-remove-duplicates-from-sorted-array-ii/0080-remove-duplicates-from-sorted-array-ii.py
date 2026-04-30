class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # given a  duplicated  in sorted array  so  we  needs to apply  two pointer  here
        a=0
        for  i in range(len(nums)):
            if a<2 or nums[i]!=nums[a-2]:
                nums[a]=nums[i]
                a+=1
        return a       