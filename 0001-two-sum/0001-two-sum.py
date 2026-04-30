class Solution(object):
    def twoSum(self, nums, target):
        """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        # #  this  can   be solved in different  ways  using  hash map  with  two poinstes 
        # # using  nexted loops   O(n2)  and 
        # for i  in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #        if nums[i]+nums[j]==target:
        #            return [i,j]
        # return None    


        #it  can  be also  solved with  order of   O(n) using hash map
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if  diff in  seen:
                return [seen[diff],i]
            seen[nums[i]]=i
        return None