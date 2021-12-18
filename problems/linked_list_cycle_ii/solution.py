# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        intersection = None
        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                intersection = fast
                break

        if intersection is not None:
            p = head
            q = intersection
            while p != q:
                p = p.next
                q = q.next

            return p