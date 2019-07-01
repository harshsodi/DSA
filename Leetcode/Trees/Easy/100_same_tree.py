# Runtime: 8 ms, faster than 99.71% of Python online submissions for Same Tree.
# Memory Usage: 11.7 MB, less than 88.10% of Python online submissions for Same Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rec(self, p, q):
        
        if not (p == None and q == None):
            try:
                if p.val != q.val:
                    return False
            except Exception:
                return False
    
        if p == None:
            return True
    
        return self.rec(p.left, q.left) and self.rec(p.right, q.right)
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return self.rec(p, q)