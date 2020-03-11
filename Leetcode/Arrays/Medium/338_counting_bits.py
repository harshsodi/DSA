# Runtime: 120 ms, faster than 21.04% of Python online submissions for Counting Bits.
# Memory Usage: 17.1 MB, less than 13.64% of Python online submissions for Counting Bits.

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # import math
        
        def get_ind(n):
            x = pow(2, int(math.log(n,2)))
            return n^x
        
        dp = {}
        dp[0] = 0
        dp[1] = 1
        
        ans = []
        
        for i in range(0, num+1):
            
            if dp.get(i) != None:
                ans.append(dp[i])
                continue
            
            tmpans = dp[get_ind(i)] + 1
            dp[i] = tmpans
            ans.append(dp[i])
            
        return ans