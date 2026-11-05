# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterate through the list. A simpler solution would be O(2n), compared to my proposed O(n)
        # solution. The O(2n) solution would be to find the number of elements in the list O(n), then
        # to find the node before the one to remove, and updating its next pointer O(n). My proposed
        # solution is to only iterate once, keeping track of which element we are at, and the node
        # that would need to be updated if we reach the end of the list, updating it after we reach
        # the end, which is O(n) time and O(1) space.

        # If there is a single element in the list, return an empty list.
        if not head.next:
            return None

        dummy = ListNode(0)
        dummy.next = head
        
        target = dummy
        trav = head
        count = 0


        while count < n:
            trav = trav.next
            count += 1

        # Now that trav and target are n + 1 nodes apart, we can increment both pointers until we
        # reach the end of the list. Once we reach the end of the list, we can set 
        # target.next = target.next.next, removing our target node from the list. In this case,
        # target isn't really the target node, but the node preceding our target node

        while trav:
            trav = trav.next
            target = target.next
        
        target.next = target.next.next
        return dummy.next
