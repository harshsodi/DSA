# Runtime: 104 ms, faster than 66.84% of Python online submissions for Linked List Components.
# Memory Usage: 20.8 MB, less than 11.11% of Python online submissions for Linked List Components.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        g = dict.fromkeys(G, True)
        ans = 0
        
        while head.next != None:
            if g.get(head.val) != None and g.get(head.next.val) == None:
                ans += 1
            head = head.next
        
        if g.get(head.val) != None:
            ans += 1
        return ans