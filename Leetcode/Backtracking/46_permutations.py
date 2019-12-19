# Runtime: 24 ms, faster than 86.24% of Python online submissions for Permutations.
# Memory Usage: 11.8 MB, less than 84.00% of Python online submissions for Permutations.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def f(arr):

            # print arr

            if len(arr) == 0:
                return []
            
            if len(arr) == 1:
                return [arr]


            p = f(arr[:-1])
            x = arr[-1]

            ans = []

            for i in p:
                # print p
                for j in range(len(i)+1):
                    ans += [i[:j] + [x] + i[j:]]

            return ans

        return f(nums)