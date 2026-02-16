class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=s.split()
        reversedString=word[::-1]
        result=" ".join(reversedString)
        return result.strip()