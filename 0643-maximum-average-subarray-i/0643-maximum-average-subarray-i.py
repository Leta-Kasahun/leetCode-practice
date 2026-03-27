class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #step 1 caculate frist sum
        prev_sum=sum(nums[:k])
        #step 2 setes the original max to compares later
        max_sum=prev_sum
        #step 3 iterates throu array startign from k  to the next
        for i in range(k,len(nums)):
            #step 4 updated by removing from the previouse  left arr and adding the right
            new_sum=prev_sum-nums[i-k]+nums[i]
            prev_sum=new_sum
            #step 5 updating the max if thire is max number 
            if new_sum>max_sum:
                max_sum=new_sum
        return max_sum/float(k)   


