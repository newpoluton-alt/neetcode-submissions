# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:    
        # initialize the list
        temp = []
        # turn linked list into simple list
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next

        # check edge case
        if len(temp) < k and len(temp) % k != 0:
            return head

        l = 0
        r = k

        while r // k <= len(temp) // k:
            temp[l: r] = temp[l: r][::-1]
            l += k
            r += k

        # turn partly reversed list into list node
        dummy = ListNode()
        tail = dummy

        for i, v in enumerate(temp):
            tail.next = ListNode(v)
            tail = tail.next

        return dummy.next