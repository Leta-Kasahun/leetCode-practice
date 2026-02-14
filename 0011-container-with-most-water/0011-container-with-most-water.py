class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
   
        """
        # 1 initialies varibles max ares to zero and index to  get O(1) using two pointer
        max_area=0
        left=0
        right=len(height)-1
        # 2 looping through it until  left < right  and assum 
        while left<right:
            # 3 the width is calculated from the distanse betwing these index.
            width=right-left
            #4 calculating the specific height  the min height to avoid over flolw
            use_h=min(height[left],height[right])
            #5 calculating the current areas from these
            curr_area=use_h*width
            #6 updating the area to the max area
            max_area=max(curr_area,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area                


