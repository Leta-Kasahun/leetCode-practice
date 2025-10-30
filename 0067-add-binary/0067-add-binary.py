class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ""
        indexa = len(a) - 1
        indexb = len(b) - 1

        while indexa >= 0 or indexb >= 0 or carry:
            if indexa >= 0:
                carry += int(a[indexa])
                indexa -= 1
            if indexb >= 0:
                carry += int(b[indexb])
                indexb -= 1

            result = str(carry % 2) + result
            carry //= 2

        return result
