# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sl = []
        for i, h in enumerate(lists):
            while h:
                sl.append(h.val)
                
                h = h.next

        sl.sort()

        nn = ListNode(0)
        dummy = nn
        for i, v in enumerate(sl):
            dummy.next = ListNode(v) # attach
            dummy = dummy.next # step forward
        return nn.next