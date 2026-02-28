class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        freq1={}
        freq2={}
        #constracting   hashtabel for this  frequency for both
        for ch in word1:
            if ch in freq1:
              freq1[ch]+=1
            else:
                freq1[ch]=1
        for ch in word2:
            if ch in freq2:
              freq2[ch]+=1
            else:
                freq2[ch]=1  
        #to check as the character  exstsis
        for ch in freq1:
            if ch not in freq2:
                return False
        for ch in freq2:
            if ch not in freq1:
                return False


        values1 = []
        for ch in freq1:
            values1.append(freq1[ch])

        values2 = []
        for ch in freq2:
            values2.append(freq2[ch])

      
        for v in values1:
            found = False
            for i in range(len(values2)):
                if values2[i] == v:
                    values2.pop(i)
                    found = True
                    break
            if not found:
                return False

        return True