# Runtime: 56 ms, faster than 99.34% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 20 MB, less than 11.36% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, p, q):
        
        # print p, q
        
        if root.val > p.val and root.val > q.val:
            return self.f(root.left, p, q)
        
        elif root.val < p.val and root.val < q.val:
            return self.f(root.right, p, q)
        
        else:
            return root
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        return self.f(root, p, q)