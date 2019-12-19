# Runtime: 36 ms, faster than 93.38% of Python online submissions for Permutations II.
# Memory Usage: 12.1 MB, less than 20.00% of Python online submissions for Permutations II.

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
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

            d = {}
            for i in p:
                # print p
                for j in range(len(i)+1):
                    tmp = i[:j] + [x] + i[j:]
                    ttmp = tuple(tmp)
                    # print ttmp
                    if d.get(ttmp) != None:
                        continue
                    d[ttmp] = True
                    ans += [tmp]

            return ans

        return f(nums)