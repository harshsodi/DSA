# Runtime: 344 ms, faster than 46.77% of Python online submissions for Remove Sub-Folders from the Filesystem.
# Memory Usage: 39.2 MB, less than 100.00% of Python online submissions for Remove Sub-Folders from the Filesystem.

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
        n = len(folder)
        
        d = {}
        ans = []
        
        for f in folder:
            d[f] = True
        
        for f in folder:
            s = ""
            valid = True
            
            for i in f:
                if i == "/" and d.get(s) != None:
                    valid = False
                    break
                s += i
                
            if valid:
                ans.append(f)
        
        return ans