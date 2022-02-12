# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mid(self, head: ListNode) -> ListNode:
        slow = fast = head
 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr is not None:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next
            
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return True
        
        mid = self.mid(head)
        
        mid = self.reverse(mid)
        
        p = head
        q = mid
        
        while p is not None and q is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        
        return True
        