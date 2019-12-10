# Runtime: 28 ms, faster than 94.32% of Python online submissions for Intersection of Two Arrays II.
# Memory Usage: 11.8 MB, less than 76.92% of Python online submissions for Intersection of Two Arrays II.


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 == 0 or n2 == 0:
            return []
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i = 0
        j = 0
        
        ans = []
        
        while i<n1 and j<n2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else :
                j += 1
        
        return ans