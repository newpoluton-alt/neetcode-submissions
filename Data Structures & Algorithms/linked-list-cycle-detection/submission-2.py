# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time and O(n) complexity
        # vals = []

        # while head:
        #     if head in vals:
        #         return True

        #     vals.append(head)
        #     head = head.next

        # return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False
