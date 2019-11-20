# Runtime: 16 ms, faster than 96.34% of Python online submissions for Rotate List.
# Memory Usage: 12 MB, less than 9.52% of Python online submissions for Rotate List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        actualHead = head
        
        n = 0
        last = head
        
        while True:
            n += 1
            if last.next == None:
                break
            else:
                last = last.next
        
        r = k%n
        first = head
        
        for i in range(n-r-1):
            first = first.next
        
        last.next = actualHead
        newHead = first.next
        first.next = None
    
        return newHead