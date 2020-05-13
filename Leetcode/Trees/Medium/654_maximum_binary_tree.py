# Runtime: 192 ms, faster than 84.81% of Python online submissions for Maximum Binary Tree.
# Memory Usage: 13.6 MB, less than 7.41% of Python online submissions for Maximum Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def f(lb, rb):
            if lb > rb:
                return None
            
            if lb == rb:
                return TreeNode(nums[lb])
            
            # Find greatest element
            indx = -1
            mx = float('-inf')
            
            for i in range(lb, rb+1):
                if nums[i] > mx:
                    mx = nums[i]
                    indx = i
            
            new_node = TreeNode(nums[indx])
            new_node.left = f(lb, indx-1)
            new_node.right = f(indx+1, rb)
            
            return new_node
        
        return f(0, len(nums)-1)