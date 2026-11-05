# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Since the numbers are in reverse order, we can compute the sum of each pair, and storing
        # that sum % 10 into the respective returning node. By keeping track of a carry bool, we
        # can also account for the overflow from the previous addition, and how that affects the 
        # sum of the next power of 10.

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            curr_sum = carry
            
            if l1:
                curr_sum += l1.val
                l1 = l1.next

            if l2:
                curr_sum += l2.val
                l2 = l2.next

            curr.next = ListNode(curr_sum % 10)
            carry = curr_sum // 10
            curr = curr.next
        
        return dummy.next
