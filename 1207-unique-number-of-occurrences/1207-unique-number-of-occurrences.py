class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen={} 
        for i in range(len(arr)):
         if arr[i]  in seen:
            seen[arr[i]]+=1
         else:
            seen[arr[i]]=1
        return len(seen.values())==len(set(seen.values()))   
               