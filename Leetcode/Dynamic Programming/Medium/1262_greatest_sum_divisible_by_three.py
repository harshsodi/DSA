# Runtime: 644 ms, faster than 5.31% of Python online submissions for Greatest Sum Divisible by Three.
# Memory Usage: 23.3 MB, less than 100.00% of Python online submissions for Greatest Sum Divisible by Three.

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dp = [[0 for i in range(3)] for j in range(n)]
        
        dp[0][nums[0]%3] = nums[0]
        
        for i in range(1, n):
            num = nums[i]
            rem = num % 3
            
            for j in range(3):
                to_update = (dp[i-1][j] + num) % 3
                        
                prev = dp[i-1][j]
                dp[i][j] = max(dp[i-1][j], dp[i][j])
                dp[i][to_update] = max([dp[i-1][to_update], prev + num, dp[i][to_update]])
            
        return dp[-1][0]