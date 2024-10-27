# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        base = 0

        base = l1.val + l2.val
        carry, base = divmod(base, 10)
        suml = ListNode(base)
        returnl = suml
        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            base = l1.val + l2.val
            carry, base = divmod(carry + base, 10)
            suml.next = ListNode(base)
            l1 = l1.next
            l2 = l2.next
            suml = suml.next
        
        while l1 is not None:
            base = l1.val
            carry, base = divmod(carry + base, 10)
            suml.next = ListNode(base)
            suml = suml.next
            l1 = l1.next
        
        while l2 is not None:
            base = l2.val
            carry, base = divmod(carry + base, 10)
            suml.next = ListNode(base)
            suml = suml.next
            l2 = l2.next
            
        if carry != 0:
            suml.next = ListNode(carry)
        return returnl
