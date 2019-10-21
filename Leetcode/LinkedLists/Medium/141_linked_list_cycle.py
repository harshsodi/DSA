# Runtime: 40 ms, faster than 59.37% of Python online submissions for Linked List Cycle.
# Memory Usage: 18.2 MB, less than 60.28% of Python online submissions for Linked List Cycle.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        p1 = head
        p2 = head
        
        if p1 == None or p2.next == None:
                return False
        
        while p1 and p2:
            
            p1 = p1.next
            
            if p1 == None or p2.next == None:
                return False
            
            p2 = p2.next.next
            
            if p1 == p2:
                break
        
        if p1 == None or p2 == None:
            return False
        return True