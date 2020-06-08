# Runtime: 20 ms, faster than 55.75% of Python online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 12.9 MB, less than 12.56% of Python online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        st = [root]
        ans = []
        
        while st != []:
            top = st.pop()
            
            if top == None:
                continue
            
            ans.append(top.val)
            
            st.append(top.left)
            st.append(top.right)
        
        return list(reversed(ans))