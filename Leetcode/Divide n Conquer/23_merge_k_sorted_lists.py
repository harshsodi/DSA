# Runtime: 192 ms, faster than 18.58% of Python online submissions for Merge k Sorted Lists.
# Memory Usage: 24.5 MB, less than 6.06% of Python online submissions for Merge k Sorted Lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        def merge(a, b):
            ans = ListNode(0)
            aans = ans
            
            while a != None and b != None:
                
                if a.val < b.val:
                    ans.next = ListNode(a.val)
                    a = a.next
                else:
                    ans.next = ListNode(b.val)
                    b = b.next
                
                ans = ans.next
            
            while a != None:
                ans.next = ListNode(a.val)
                ans = ans.next
                a = a.next
            
            while b != None:
                ans.next = ListNode(b.val)
                ans = ans.next
                b = b.next
            
            return aans.next
        
        def divide(lists, l, r):
            
            if l == r:
                return lists[l]
        
            m = (l+r)/2
            
            if l < r:
                lft = divide(lists, l, m)
                rgt = divide(lists, m+1, r)

                return merge(lft, rgt)
        
            return None
        
        return divide(lists, 0, len(lists) - 1)