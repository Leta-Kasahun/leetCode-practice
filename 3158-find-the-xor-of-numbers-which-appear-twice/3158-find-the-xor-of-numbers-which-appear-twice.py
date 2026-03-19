class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        result=0
        for num in nums:
            seen[num]=seen.get(num,0)+1
        for num in seen:
            if seen[num]==2:
                result^=num
                
        return result   
