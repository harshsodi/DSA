# Runtime: 88 ms, faster than 81.10% of Python online submissions for Top K Frequent Elements.
# Memory Usage: 15.2 MB, less than 87.81% of Python online submissions for Top K Frequent Elements.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        sorted_x = sorted(d.items(), key = lambda k: k[1], reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(sorted_x[i][0])
        
        return ans