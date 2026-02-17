class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sb=tb=0
        while sb<len(s) and tb<len(t):
            if s[sb] == t[tb]:
                sb+=1 
            tb+=1
        return sb==len(s)        
        
        