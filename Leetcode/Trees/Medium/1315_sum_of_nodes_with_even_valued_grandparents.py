# Runtime: 88 ms, faster than 100.00% of Python online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 19.4 MB, less than 100.00% of Python online submissions for Sum of Nodes with Even-Valued Grandparent.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        
        def f(root, family):
            
            if family[0] and family[0] % 2 == 0:
                self.ans += root.val
            
            if root.left:
                f(root.left, (family[1], root.val))
            
            if root.right:
                f(root.right, (family[1], root.val))
        
        f(root, (None, None))
        
        return self.ans