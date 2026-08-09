# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        carry = 0
        dummy = ListNode()
        tail = dummy

        while carry or q or p:
            x = p.val if p else 0
            y = q.val if q else 0

            s = x + y + carry

            carry = s // 10
            tail.next = ListNode(s % 10)
            tail = tail.next
            p = p.next if p else None
            q = q.next if q else None

        return dummy.next

        

            