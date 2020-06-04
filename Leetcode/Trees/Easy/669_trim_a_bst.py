# Runtime: 40 ms, faster than 83.23% of Python online submissions for Trim a Binary Search Tree.
# Memory Usage: 20.4 MB, less than 100.00% of Python online submissions for Trim a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        def f(root):
            
            if root == None:
                return None
            
            if root.val < L:
                return f(root.right)
            elif root.val > R:
                return f(root.left)
            else:
                root.left = f(root.left)
                root.right = f(root.right)
                
                return root
        
        return f(root)