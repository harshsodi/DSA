# Runtime: 16 ms, faster than 94.25% of Python online submissions for Split Array Largest Sum.
# Memory Usage: 11.8 MB, less than 85.71% of Python online submissions for Split Array Largest Sum.

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        def can_split(arr, m, limit):
            n = len(arr)

            s = 0
            i = 0
            m_curr = 1

            while i < n:
                ts = s + arr[i]

                if ts > limit:
                    m_curr += 1

                    if m_curr > m:
                        return True

                    s = arr[i]
                else:
                    s = ts

                i += 1

            return False
    
        l = max(nums)
        r = sum(nums)
    
        # print l, r
        
        while l < r:
            mid = (l+r)/2
            
            if can_split(nums, m, mid):
                l = mid + 1
            else:
                r = mid
        
        return r