# Runtime: 24 ms, faster than 80.78% of Python online submissions for Relative Sort Array.
# Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Relative Sort Array.

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        d2 = dict.fromkeys(arr2, True)
        d1 = {}
        
        for i in arr1:
            if d2.get(i):
                d1[i] = d1.get(i, 0) + 1
            else:
                d1[-1] = d1.get(-1, []) + [i]
        
        ans = []
        for i in range(len(arr2)):
            for j in range(d1[arr2[i]]):
                ans.append(arr2[i])
        
        for i in sorted(d1.get(-1, [])):
            ans.append(i)
        
        return ans