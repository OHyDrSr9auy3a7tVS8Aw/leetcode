# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        e_head = None
        e_curr = None
        e_prev = None

        prev = None
        curr = head

        is_even = False
        
        while curr is not None:
            if is_even:
                if e_head is None:
                    e_head = curr
                    e_curr = e_head
                else:
                    e_curr.next = curr
                    e_prev, e_curr = e_curr, e_curr.next

                curr = curr.next
                prev.next = curr

            else:
                prev, curr = curr, curr.next

            is_even ^= True

        if e_curr is not None:
            e_curr.next = None
        prev.next = e_head

        return head
            
        