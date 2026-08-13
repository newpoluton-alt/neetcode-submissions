# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:    
        # # initialize the list
        # temp = []
        # # turn linked list into simple list
        # curr = head
        # while curr:
        #     temp.append(curr.val)
        #     curr = curr.next

        # # check edge case
        # if len(temp) < k and len(temp) % k != 0:
        #     return head

        # l = 0
        # r = k

        # while r // k <= len(temp) // k:
        #     temp[l: r] = temp[l: r][::-1]
        #     l += k
        #     r += k

        # # turn partly reversed list into list node
        # dummy = ListNode()
        # tail = dummy

        # for i, v in enumerate(temp):
        #     tail.next = ListNode(v)
        #     tail = tail.next

        # return dummy.next

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr