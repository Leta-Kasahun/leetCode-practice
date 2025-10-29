class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        for i in range(n-1,-1,-1):
            digits[i]+=1
            if digits[i]<10:
                return digits
            else:
                digits[i]=0
        return digits+[1]            