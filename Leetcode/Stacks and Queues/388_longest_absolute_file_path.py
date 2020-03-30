# Runtime: 12 ms, faster than 91.80% of Python online submissions for Longest Absolute File Path.
# Memory Usage: 12.7 MB, less than 7.69% of Python online submissions for Longest Absolute File Path.

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        lines = [[y + "/" for y in x.split("\t")] for x in (input.split("\n"))]
        
        st = []
        
        n = len(lines)
        ans = 0
        tlen = 0
        
        for i in range(n):
            
            line = lines[i]
            level = len(line)
            word = line[-1]
            
            while st != [] and level <= st[-1][1]:
                topline = st.pop()
                tlen -= len(topline[0])                
            
            st.append([word, level])
            tlen += len(word)
            
            if '.' in word:
                ans = max(tlen, ans)
        
        return max(0, ans - 1)