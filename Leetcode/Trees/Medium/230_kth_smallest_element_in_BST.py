# Runtime: 40 ms, faster than 78.87% of Python online submissions for Kth Smallest Element in a BST.
# Memory Usage: 19.7 MB, less than 15.22% of Python online submissions for Kth Smallest Element in a BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        st = []
        
        while True:
            while root:
                st.append(root)
                root = root.left
            
            root = st.pop()
            k -= 1
            
            if k == 0:
                return root.val
            
            root = root.right