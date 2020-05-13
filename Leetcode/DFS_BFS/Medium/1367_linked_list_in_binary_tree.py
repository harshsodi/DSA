# Runtime: 104 ms, faster than 77.54% of Python online submissions for Linked List in Binary Tree.
# Memory Usage: 15.5 MB, less than 100.00% of Python online submissions for Linked List in Binary Tree.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        self.ahead = head
        self.mem = {}
        
        def f(root, exp):
          
            if root == None:
                return False
        
            return is_path(root, exp) or f(root.left, self.ahead) or f(root.right, self.ahead) 
    
        def is_path(root, exp):
            
            if exp == None:
                return True
            
            if root == None or root.val != exp.val:
                return False
        
            return is_path(root.left, exp.next) or is_path(root.right, exp.next)
        
        return f(root, self.ahead)