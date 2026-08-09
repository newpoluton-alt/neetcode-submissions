# LeetCode-style ListNode is assumed
# from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Find middle (slow ends at tail of first half)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half
        second = slow.next
        slow.next = None
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev  # head of reversed half

        # 3) Merge two halves: head (first), second (reversed)
        first = head
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
