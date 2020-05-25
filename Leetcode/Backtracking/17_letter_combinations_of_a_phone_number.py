# Runtime: 16 ms, faster than 82.45% of Python online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 12.7 MB, less than 7.14% of Python online submissions for Letter Combinations of a Phone Number.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        self.n = len(digits)
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digs = [int(dig) for dig in digits]
        
        def f(i, cstr):
            
            if i == self.n:
                self.ans.append(cstr)
                return
            
            for j in d[digs[i]]:
                f(i+1, cstr + j)
        
        self.ans = []
        f(0, "")
        
        return self.ans