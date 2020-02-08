# Runtime: 376 ms, faster than 99.67% of Python online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 83.8 MB, less than 100.00% of Python online submissions for Maximum Product of Splitted Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        CAP = 1000000007
        
        ans = float('-inf')
        sums = []
        
        def f(root):
            
            if root == None:
                return 0
            
            lsum = f(root.left)
            rsum = f(root.right)
            
            a = root.val + lsum + rsum
            sums.append(a)
            
            return a
    
        total = f(root)
                 
        # print sums
        # print total
        
        for s in sums:
            ans = max(ans, (s*(total-s)))
        
        return ans % CAP