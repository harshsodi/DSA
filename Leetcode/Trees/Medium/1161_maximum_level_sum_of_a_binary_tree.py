# Runtime: 372 ms, faster than 40.21% of Python online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 20 MB, less than 100.00% of Python online submissions for Maximum Level Sum of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        max_sum = root.val
        ans = 1
        
        level = 1
        q = [root]
        
        while len(q):
            next_level = []
            curr_sum = 0
            
            for i in range(len(q)):
                top = q.pop(0)
                
                if top.left != None:
                    next_level.append(top.left)
                    curr_sum += top.left.val
                
                if top.right != None:
                    next_level.append(top.right)
                    curr_sum += top.right.val
            
            level += 1
            
            if max_sum < curr_sum:
                ans = level
                max_sum = curr_sum
            
            q = next_level
        
        return ans