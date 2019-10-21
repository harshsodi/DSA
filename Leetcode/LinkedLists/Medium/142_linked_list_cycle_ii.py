# Runtime: 44 ms, faster than 45.90% of Python online submissions for Linked List Cycle II.
# Memory Usage: 18.2 MB, less than 60.38% of Python online submissions for Linked List Cycle II.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1 = head
        p2 = head
        
        while p1 and p2:
            
            p1 = p1.next
            
            if p1 == None or p2.next == None:
                return None
            
            p2 = p2.next.next
            
            if p1 == p2:
                break
        
        if p1 == None or p2 == None:
            return None
        
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1