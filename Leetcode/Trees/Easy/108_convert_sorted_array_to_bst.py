# Runtime: 48 ms, faster than 95.81% of Python online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 16.1 MB, less than 22.73% of Python online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, l, r, nums):
        
        m = (l+r)/2
        print l, m, r
        
        root = TreeNode(nums[m])
        
        if m>l:
            root.left = self.f(l, m-1, nums)
        if m<r:
            root.right = self.f(m+1, r, nums)
        
        return root 
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        l = len(nums)
        
        if l==0:
            return None
        
        return self.f(0, l-1, nums)
        