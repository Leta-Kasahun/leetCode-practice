class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #step 1 begning from last right most
        i=len(num1)-1
        j=len(num2)-1

        #step 2 intionalizes carry to adds from rignt to left
        carry=0
        result=""
        #step3 itrating untill the values of i and j is becames 0 and there is craay
        while j>=0 or i>=0 or carry:
            #step4 converting to number by unsing ord to convergetes  to thie ascci char
            d1=ord(num1[i])-ord('0') if i>=0 else 0 
            d2=ord(num2[j])-ord('0') if j>=0 else 0
            # if i>=0 else 0 is used to itrate only upto left most even j is greates digit
            #step5 adding tootal
            total=d1+d2+carry
            #step6 converting aschid to strign and set result
            result=chr(total%10+ ord('0'))+result
            #total%10 this is used to get the last digit
            #step7 calcultaitng the carry from the
            carry=total//10
            #step 8 decrepete both  i and j
            j-=1
            i-=1
        return result    

        

            

        