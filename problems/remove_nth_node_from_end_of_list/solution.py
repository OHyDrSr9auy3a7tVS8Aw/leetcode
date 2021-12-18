# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return
        
        curr = head
        size = 0
        
        while curr.next is not None:
            curr = curr.next
            size += 1
            
        idx = size - n + 1
        
        if idx == 0:
            return head.next
        
        curr = head
        for _ in range(idx):
            prev, curr = curr, curr.next
            
        prev.next = curr.next
        
        return head
        