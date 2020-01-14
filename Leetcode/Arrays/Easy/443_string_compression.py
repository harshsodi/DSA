# Runtime: 40 ms, faster than 89.20% of Python online submissions for String Compression.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for String Compression.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        chars.append(chr(34))
        n = len(chars)
        
        c = 0
        fr = 1
        
        i = 1
        while i < n:
            
            if chars[i] != chars[i-1]:
                chars[c] = chars[i-1]
                c += 1
                
                if fr > 1:
                    fstr = str(fr)
                    
                    for ch in fstr:
                        chars[c] = ch
                        c += 1
                    
                fr = 1    
                
            else:
                fr += 1
                    
            i += 1
    
        return c