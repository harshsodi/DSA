# Runtime: 16 ms, faster than 85.07% of Python online submissions for Permutation Sequence.
# Memory Usage: 11.8 MB, less than 16.67% of Python online submissions for Permutation Sequence.

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        facts = [1 for _ in range(n+1)]
        for i in range(1, n+1):
            facts[i] = i * facts[i-1]
        
        def f(arr, k_):
            
            if k_ == 0:
                return arr
            
            n_ = len(arr)
            f_ = facts[n_-1]
            
            ch = k_ / f_
            rem = k_%f_
            
            return [arr[ch]] + f(arr[:ch] + arr[ch+1:], rem)
        
        a = [str(x) for x in range(1, n+1)]
        ans = f(a, k-1)
        
        return "".join(ans)