# Runtime: 28 ms, faster than 48.26% of Python online submissions for Distribute Coins in Binary Tree.
# Memory Usage: 12.9 MB, less than 33.33% of Python online submissions for Distribute Coins in Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        
        def f(root):
            
            if root == None:
                return 0
        
            l = f(root.left)
            r = f(root.right)
            
            tmp = (root.val - 1) + l + r
            self.ans += abs(tmp)
            
            return tmp
    
        f(root)
        return self.ans
    