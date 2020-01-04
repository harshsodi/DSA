# Runtime: 32 ms, faster than 96.78% of Python online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 14.1 MB, less than 100.00% of Python online submissions for Populating Next Right Pointers in Each Node II.

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
        
        # BFS
        
        q = [root, None]
        
        while len(q):
            next_level = []
            lq = len(q)
            
            for node_ in range(lq):    
                node = q.pop(0)
                if node:
                    node.next = q[0]
                
                    left = node.left
                    right = node.right

                    if left:
                        next_level.append(node.left)
                    if right:
                        next_level.append(node.right)
            
            if len(next_level):
                next_level.append(None)
            # print next_level
            
            q = next_level
        
        return root