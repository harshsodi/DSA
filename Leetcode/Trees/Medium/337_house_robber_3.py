# Runtime: 68 ms, faster than 15.48% of Python online submissions for House Robber III.
# Memory Usage: 19 MB, less than 5.34% of Python online submissions for House Robber III.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.mem = {}
        def f(root, loot):
                    
            if root == None:
                return 0
        
            if self.mem.get((root, loot)):
                return self.mem[(root, loot)]
        
            ans = float('-inf')
            
            if loot == True:
                ans = max(ans, root.val + f(root.left, False) + f(root.right, False))
                
            ans = max(ans, f(root.left, True) + f(root.right, True))
            
                            
            self.mem[(root, loot)] = ans
            return ans
    
        return f(root, True)