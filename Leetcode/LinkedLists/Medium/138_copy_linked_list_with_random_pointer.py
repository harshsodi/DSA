# Runtime: 68 ms, faster than 84.33% of Python online submissions for Copy List with Random Pointer.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Copy List with Random Pointer.

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        actualHead = head
    
        # Create basic linked list
    
        if head == None:
            return None
    
        head2 = Node(head.val)
        actualHead2 = head2
    
        nodepos = {}
        curr = 0
        while head:
            nodepos[head] = curr
            head = head.next
            curr += 1
        
        # Creat basic linked list and make list of nodes as in position
                
        head = actualHead
        nodepos2 = []
        nodepos2.append(head2)
        
        while head:
            nextNode = None
            if head.next:
                nextNode = Node(head.next.val)
            head2.next = nextNode
            
            nodepos2.append(nextNode)
            
            head = head.next
            head2 = head2.next
        
        # print nodepos2
        
        # Fill in the random pointers
        head = actualHead
        head2 = actualHead2
        
        while head:
            if head.random == None:
                head2.random = None
            else:
                head2.random = nodepos2[nodepos[head.random]]
                
            head = head.next
            head2 = head2.next
                
        
        return actualHead2