# Runtime: 16 ms, faster than 73.21% of Python online submissions for Print Words Vertically.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Print Words Vertically.

class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ans = []
        mat = [x for x in s.split(" ")]
        
        maxlen = max([len(x) for x in mat])
        n = len(mat)
        
        for i in range(maxlen):
            word = ""
            for j in range(n):
                if len(mat[j])-1 < i:
                    word += " "
                else:
                    word += mat[j][i]
            
            i = len(word) - 1
            while word[i] == " ":
                i -= 1
            
            ans.append(word[:i+1])
    
        return ans