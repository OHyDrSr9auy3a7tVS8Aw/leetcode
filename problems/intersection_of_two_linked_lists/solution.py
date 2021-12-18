# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_a = set()
        seen_b = set()
        
        a = headA
        b = headB
        
        while not (a is None and b is None):
            seen_a.add(a)
            seen_b.add(b)    
            
            if a is not None:
                a = a.next
            if b is not None:
                b = b.next
                
            intersect = seen_a & seen_b
            if len(intersect) == 1:
                return intersect.pop()

        