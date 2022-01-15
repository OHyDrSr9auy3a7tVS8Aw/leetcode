# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return

        prev = None
        curr = head

        while curr is not None:
            if curr.val == val:
                if prev is None:
                    curr = curr.next
                    head = curr
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev, curr = curr, curr.next

        return head