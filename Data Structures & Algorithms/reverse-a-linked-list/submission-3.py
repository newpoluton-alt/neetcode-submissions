# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [0, 1, 2, 3]
        # [1, 2, 3]
        # [2, 3]
        # [3]
        # [Null]
        
        if not head:
            return None
        
        # [0, 1, 2, 3]
        # [1, 2, 3]
        # [2, 3]
        # [3]
        # [Null]
        newHead = head

        # [1, 2, 3]
        # [2, 3]
        # [3]
        if head.next:
            # [1, 2, 3]
            # [2, 3]
            # [3]
            # [Null]
            newHead = self.reverseList(head.next)
            # [Null, 3]
            # [Null, 3, 2]
            # [Null, 3, 2, 1]
            # [Null, 3, 2, 1, 0]
            head.next.next = head
  
        head.next = None

        return newHead