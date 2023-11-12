# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry: int = 0
        base: int = 0

        return_l: Optional[ListNode] = ListNode()
        sum_l: Optional[ListNode] = return_l

        while l1 != None and l2 != None:
            base = l1.val + l2.val + carry
            carry = base//10
            base = base % 10

            return_l.next = ListNode(base)

            return_l = return_l.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            base = l1.val + carry
            carry = base//10
            base = base % 10

            return_l.next = ListNode(base)

            return_l = return_l.next
            l1 = l1.next
        
        while l2 != None:
            base = l2.val + carry
            carry = base//10
            base = base % 10

            return_l.next = ListNode(base)

            return_l = return_l.next
            l2 = l2.next
        
        if carry > 0:
            return_l.next = ListNode(carry)
        
        return sum_l.next

        