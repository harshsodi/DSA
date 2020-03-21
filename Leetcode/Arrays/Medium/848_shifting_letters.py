# Runtime: 192 ms, faster than 31.11% of Python online submissions for Shifting Letters.
# Memory Usage: 14.5 MB, less than 33.33% of Python online submissions for Shifting Letters.

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        
        n = len(S)
        
        ans = ""
        cnt = 0
        
        i = n-1
        while i >= 0:
            cnt += shifts[i]
            
            curr_ch = ord(S[i]) - ord('a')
            next_ch = (curr_ch + cnt)%26 + ord('a')
            
            ans = chr(next_ch) + ans
        
            i -= 1
        
        return ans