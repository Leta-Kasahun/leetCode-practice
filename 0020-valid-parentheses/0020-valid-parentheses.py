class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={')':'(','}':'{',']':'['}
        opening=pairs.values()
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1]!=pairs[char]:
                    return False
                stack.pop()
        return len(stack)==0                    
