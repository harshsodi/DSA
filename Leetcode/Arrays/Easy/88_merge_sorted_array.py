# Runtime: 12 ms, faster than 99.84% of Python online submissions for Merge Sorted Array.
# Memory Usage: 11.7 MB, less than 85.74% of Python online submissions for Merge Sorted Array.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        newarr = []
        i1 = 0
        i2 = 0
        
        while i1 < m and i2 < n:
            if nums1[i1] < nums2[i2]:
                newarr.append(nums1[i1])
                i1 += 1
            else:
                newarr.append(nums2[i2])
                i2 += 1
        
        while i1 < m:
            newarr.append(nums1[i1])
            i1 += 1
        
        while i2 < n:
            newarr.append(nums2[i2])   
            i2 += 1
        
        print newarr
        for i in range(len(nums1)):
            nums1[i] = newarr[i]