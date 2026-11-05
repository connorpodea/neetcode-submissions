# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        linked = dummy

        curr_l1 = list1
        curr_l2 = list2

        while curr_l1 is not None and curr_l2 is not None:
            if curr_l1.val < curr_l2.val:
                linked.next = curr_l1
                curr_l1 = curr_l1.next
            else:
                linked.next = curr_l2
                curr_l2 = curr_l2.next
            
            linked = linked.next

        # Attach the entire remaining list in a single line.
        if curr_l1 is not None:
            linked.next = curr_l1
        else:
            linked.next = curr_l2
        
        # Return dummy.next because dummy itself is just our fake placeholder.
        return dummy.next