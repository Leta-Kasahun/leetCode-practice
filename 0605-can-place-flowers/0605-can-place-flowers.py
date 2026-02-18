class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m=len(flowerbed)
        for i in range(m):
         if flowerbed[i]==0:
            left=(i==0 or flowerbed[i-1]==0)
            right=(i==m-1 or flowerbed[i+1]==0)
            if left and right:
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        return n<=0            

        