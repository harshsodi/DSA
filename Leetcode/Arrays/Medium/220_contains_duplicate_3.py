# Runtime: 48 ms, faster than 55.39% of Python online submissions for Contains Duplicate III.
# Memory Usage: 15.6 MB, less than 33.33% of Python online submissions for Contains Duplicate III.

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        n = len(nums)
        pairs = [(nums[i], i) for i in range(n)]
        pairs = sorted(pairs, key=lambda x: x[0])
        
        l = 0
        r = 1
        
        while r < n:
            if l == r:
                if r >= n-1:
                    return False
                else:
                    r += 1
            else:
                if abs(pairs[l][0] - pairs[r][0]) <= t:
                    if abs(pairs[l][1] - pairs[r][1]) <= k:
                        return True
                    r += 1
                else:
                    l += 1