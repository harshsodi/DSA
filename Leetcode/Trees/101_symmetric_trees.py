
# Runtime: 12 ms, faster than 99.44% of Python online submissions for Symmetric Tree.
# Memory Usage: 12 MB, less than 69.85% of Python online submissions for Symmetric Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rec(self, isRoot, l, r):
        
        if isRoot:
            if not l:
                return True
            return self.rec(False, l.left, l.right)
        if (l == None and r == None):
            return True
        if (l != None or r != None):
            try:
                if l.val != r.val:
                    return False
            except Exception:
                return False
    
        return self.rec(False, l.left, r.right) and self.rec(False, l.right, r.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.rec(True, root, root)