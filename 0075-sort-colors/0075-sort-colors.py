class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = medium = 0
        high = len(nums) - 1

        while medium <= high:
            if nums[medium] == 0:
                nums[low], nums[medium] = nums[medium], nums[low]
                low += 1
                medium += 1
            elif nums[medium] == 1:
                medium += 1
            else:  # nums[medium] == 2
                nums[medium], nums[high] = nums[high], nums[medium]
                high -= 1
