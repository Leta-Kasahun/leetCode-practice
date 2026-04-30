class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # it is given sorted duplicated array
        #tasks is  to  modifies the  array and make uiques  and then return  unique num
        # this  needs to be solved using two pointer array  to  be  O(n)
        a=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                a+=1
                nums[a]=nums[i]
        return a+1        


