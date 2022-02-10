# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        intersect = None        
        slow = fast = head
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                intersect = slow
                break
    
        if intersect is None:
            return
        
        p = head
        q = intersect
        
        while p != q:
            p = p.next
            q = q.next
            
        return p