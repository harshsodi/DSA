# Runtime: 3924 ms, faster than 5.20% of Python online submissions for Palindrome Pairs.
# Memory Usage: 14.4 MB, less than 10.00% of Python online submissions for Palindrome Pairs.

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        def reverse(s):
            if len(s) == 0:
                return s
            else:
                return reverse(s[1:]) + s[0]
        
        def is_palin(s):
            n = len(s)
            l = 0
            r = n - 1
            
            while l < r:
                if s[l] != s[r]:
                    return False
            
                l += 1
                r -= 1
            
            return True

        ans = []
        d = {}
        for i in range(len(words)):
            d[words[i]] = i
            
        # print d
        
        for w in range(len(words)):
            word = words[w]
            rev = reverse(word)
            
            if d.get(rev) != None:
                if d[rev] != w:
                    ans.append([w, d[rev]])
            
            l = len(word)
            for k in range(l):
                # Check prefix
                pref = word[:k+1]
                prefrem = word[k+1:]
                remrev = reverse(prefrem)
                
                if is_palin(pref):
                    if d.get(remrev) != None:
                        ans.append([d[remrev], w])
                
                # Check suffix
                suff = word[k:]
                suffrem = word[:k]
                remrev = reverse(suffrem)
                
                if is_palin(suff):
                    if d.get(remrev) != None:
                        ans.append([w, d[remrev]])
        
        return ans