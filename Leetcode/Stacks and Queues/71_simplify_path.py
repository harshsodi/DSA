# Runtime: 24 ms, faster than 53.88% of Python online submissions for Simplify Path.
# Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Simplify Path.

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        path = path + "/"
        components = []
        
        word = ""
        for i in path:
            if i == "/":
                
                if word == "..":
                    if len(components):
                        components.pop()
                elif word != "." and word != "":
                    components.append(word)
                
                word = ""
                continue
        
            word += i
        
        return "/" + "/".join(components)   