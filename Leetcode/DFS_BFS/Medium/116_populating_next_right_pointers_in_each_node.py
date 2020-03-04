# Runtime: 56 ms, faster than 56.75% of Python online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 14.8 MB, less than 8.00% of Python online submissions for Populating Next Right Pointers in Each Node.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root == None:
            return None
        
        q = [root]
        
        while len(q):
            
            next_level = []
            
            l = len(q)
            for i in range(l):
                
                if i < l - 1:
                    q[i].next = q[i+1]
                
                if q[i].left != None:
                    next_level.append(q[i].left)
                    next_level.append(q[i].right)
            
            q = next_level
        
        return root