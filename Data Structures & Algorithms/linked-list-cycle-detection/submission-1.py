# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vals = []

        while head:
            if head in vals:
                return True

            vals.append(head)
            head = head.next

        return False