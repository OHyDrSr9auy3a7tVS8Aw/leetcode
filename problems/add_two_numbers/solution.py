# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from copy import deepcopy

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        a = 0
        b = 0
        
        place = 1
        while True:
            a += l1.val * place
            place *= 10
            l1 = l1.next
            if l1 is None:
                break
                
        place = 1      
        while True:
            b += l2.val * place
            place *= 10
            l2 = l2.next
            if l2 is None:
                break
                
                
        c = a + b
        print(a, b, c)

        c = [int(i) for i in list(str(c))]
        print(c)
        
        l3 = ListNode(c[0])
            
        for s in c[1:]:
            print(l3)
            l3.next = deepcopy(l3)
            l3.val = s
            
        return l3
            
            
        