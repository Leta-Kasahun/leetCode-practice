class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=str(x)
        for i in range(len(num)):
            num=[num::-1]
        return int(num)

