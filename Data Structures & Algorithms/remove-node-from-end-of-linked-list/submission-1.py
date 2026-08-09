# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)          # guard to handle deleting the head
        fast = slow = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # advance both until fast hits the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # delete the nth from end (slow is just before target)
        slow.next = slow.next.next

        return dummy.next    