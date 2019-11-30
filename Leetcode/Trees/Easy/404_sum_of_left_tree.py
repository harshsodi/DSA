# Runtime: 8 ms, faster than 99.59% of Python online submissions for Sum of Left Leaves.
# Memory Usage: 12.6 MB, less than 25.00% of Python online submissions for Sum of Left Leaves.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, isLeft):
        
        if root == None:
            return
        
        if root.left == None and root.right == None:
            self.ans += root.val * isLeft
        
        if root.left:
            self.f(root.left, 1)
        
        if root.right:
            self.f(root.right, 0)
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        self.f(root, 0)
        
        return self.ans