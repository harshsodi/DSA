# Runtime: 32 ms, faster than 96.29% of Python online submissions for Balanced Binary Tree.
# Memory Usage: 16.2 MB, less than 100.00% of Python online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, d):
        if root == None or self.ans == False:
            return d
    
        lh = self.f(root.left, d+1)
        rh = self.f(root.right, d+1)
        
        if abs(lh - rh) > 1:
            self.ans = False
            return 0
        
        return max(lh, rh)
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.ans = True
        self.f(root, 0)
        
        return self.ans