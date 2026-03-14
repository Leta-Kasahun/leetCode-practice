class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #step 2 convertes to sets  to make  unique
        n1=set(nums1)
        n2=set(nums2)
        
        #step 2 find thier intersectuiot  that is found in both
        
        return list(n1 & n2)