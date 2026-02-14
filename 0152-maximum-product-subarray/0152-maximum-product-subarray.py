class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=max(nums)
        max_product=1
        min_product=1
        for n in nums:
            curr_product=max_product*n
            max_product=max(curr_product,min_product*n,n)
            min_product=min(curr_product,min_product*n,n)
            result=max(result,max_product)
        return result    
                

