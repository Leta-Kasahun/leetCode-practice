class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        for n in seen:
            if seen[n]==1:
                return n    