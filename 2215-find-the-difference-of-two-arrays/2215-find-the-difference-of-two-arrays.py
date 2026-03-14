class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        #step converting to set to make uniqui
        n1=set(nums1)
        n2=set(nums2)
        #step find the difference to get elemtes that is appear only in one of the two
        r1=list(n1-n2)
        r2=list(n2-n1)
        return [r1,r2]