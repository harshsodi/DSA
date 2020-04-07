# Runtime: 32 ms, faster than 77.05% of Python online submissions for Diameter of Binary Tree.
# Memory Usage: 15.7 MB, less than 7.69% of Python online submissions for Diameter of Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def f(root):
            if root == None:
                self.ans = max(self.ans, 0)
                return -1
            
            l = f(root.left) + 1
            r = f(root.right) + 1
        
            self.ans = max(self.ans, l + r)
        
            return max(l, r)
        
        self.ans = float('-inf')
        f(root)
        
        return self.ans