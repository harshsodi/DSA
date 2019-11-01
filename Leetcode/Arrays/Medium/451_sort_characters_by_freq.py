# Runtime: 48 ms, faster than 71.82% of Python online submissions for Sort Characters By Frequency.
# Memory Usage: 14.3 MB, less than 55.56% of Python online submissions for Sort Characters By Frequency.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        freq = {}
        
        for c in s:
            if not freq.get(c):
                freq[c] = 0
            freq[c] += 1
        
        sorted_x = sorted(freq.items(), key = lambda k: k[1], reverse=True)
        
        ans = ''
        for x in sorted_x:
            ans += x[0] * x[1]
        return ans