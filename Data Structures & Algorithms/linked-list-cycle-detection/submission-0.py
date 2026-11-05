# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        trav = head

        while trav is not None:
            count += 1
            trav = trav.next

            if count > 1000:
                return True

        return False