# Runtime: 108 ms, faster than 14.32% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 27.6 MB, less than 18.57% of Python online submissions for Lowest Common Ancestor of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        self.ans = None
        
        def f(root):
            
            if root == None:
                return [False, False]
            
            l = f(root.left)
            r = f(root.right)
            
            if root == p:
                if l[1] or r[1]:
                    self.ans = root
                    return [True, True]
                return [True, False]
            
            if root == q:
                if l[0] or r[0]:
                    self.ans = root
                    return [True, True]
                return [False, True]
            
            ret = [l[0] or r[0], l[1] or r[1]]
            if ret == [True, True] and self.ans == None:
                self.ans = root
            
            return ret
    
        f(root)
        
        return self.ans