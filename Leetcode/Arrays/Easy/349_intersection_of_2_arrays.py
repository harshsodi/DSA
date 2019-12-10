# Runtime: 24 ms, faster than 97.72% of Python online submissions for Intersection of Two Arrays.
# Memory Usage: 12.1 MB, less than 5.56% of Python online submissions for Intersection of Two Arrays.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        d = {}
        
        for i in nums1:
            d[i] = True
        
        ans = []
        
        for i in nums2:
            if d.get(i):
                ans.append(i)
                
        return list(set(ans))