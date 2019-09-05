# Runtime: 20 ms, faster than 73.41% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.9 MB, less than 57.50% of Python online submissions for Longest Common Prefix.

class Solution(object):
    def longestCommonPrefix(self, arr):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if arr == []:
            return ""
        
        min_len = len(arr[0])
        for i in arr:
            min_len = min(min_len, len(i))
        
        same_till = -1
        broken = False
        for i in range(min_len):
            for s in arr:
                if s[i] != arr[0][i]:
                    broken = True
                    break
            
            if broken:
                break
            else:
                same_till = i
        
        return arr[0][:same_till+1]