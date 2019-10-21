# Runtime: 32 ms, faster than 86.41% of Python online submissions for Next Greater Element I.
# Memory Usage: 12 MB, less than 14.29% of Python online submissions for Next Greater Element I.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        n = len(nums2)
        
        s = []
        ans = {}
            
        for i in range(n):
            if len(s) > 0:
                while len(s) and nums2[s[-1]] < nums2[i]:
                    ans[nums2[s.pop()]] = nums2[i]
                
            s.append(i)
        
        a = []
        for i in nums1:
            a.append(ans.get(i, -1))

        return a