# Runtime: 316 ms, faster than 99.01% of Python online submissions for Balance a Binary Search Tree.
# Memory Usage: 21.1 MB, less than 96.53% of Python online submissions for Balance a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        arr = []
        
        def f(root):
            
            if root == None:
                return
            
            f(root.left)
            arr.append(root)
            f(root.right)
        
        f(root)
        
        def build(l, r):
            
            # print l, r
            
            if l > r:
                return None
            
            if l == r:
                arr[l].left, arr[l].right = None, None
                return arr[l]
            
            m = (l+r)/2
            arr[m].left = build(l, m-1)
            arr[m].right = build(m+1, r)
            
            return arr[m]
    
        return build(0, len(arr) - 1)