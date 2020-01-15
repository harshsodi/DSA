# Runtime: 60 ms, faster than 81.00% of Python online submissions for Compare Strings by Frequency of the Smallest Character.
# Memory Usage: 12.3 MB, less than 100.00% of Python online submissions for Compare Strings by Frequency of the Smallest Character.

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        
        def f(s):
            d = {}
            for ch in s:
                d[ch] = d.get(ch,0) + 1
            
            for x in 'abcdefghijklmnopqrstuvwxyz':
                if d.get(x):
                    return d[x]
        
        words_map = [0 for _ in range(11)]
        words_sum = [0 for _ in range(11)]
    
        for w in words:
            w_ = f(w)
            words_map[w_] += 1
    
        sm = 0
        for i in range(11):
            sm += words_map[10-i]
            words_sum[10-i] = sm
       
        # print words_map
        # print words_sum
    
        ans = []
        
        for q in queries:
            q_ = f(q)
            ans.append(words_sum[q_] - words_map[q_])
        
        return ans