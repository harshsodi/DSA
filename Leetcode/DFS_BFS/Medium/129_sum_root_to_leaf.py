# Runtime: 20 ms, faster than 65.44% of Python online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 12.2 MB, less than 13.64% of Python online submissions for Sum Root to Leaf Numbers.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def f(root, x):
        
            if root == None:
                return 0
        
            if root.left == None and root.right == None:
                return (x*10) + (root.val)
            
            l = f(root.left, (x*10)+(root.val))
            r = f(root.right, (x*10)+(root.val))
            
            return l + r
    
        return f(root, 0)