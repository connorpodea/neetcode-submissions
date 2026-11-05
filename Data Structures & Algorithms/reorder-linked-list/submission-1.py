# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First, we want to split the list in half.
        # Then, we want to take the second half and reverse it.
        # By splitting the list and reversing the second half, we can use
        # two pointers to recreate a list in the desired order

        # To split the list, we can use slow fast pointers, iterating until fast or fast.next is nil.
        # This implies that our second half begins where slow is.
        # If the number of elements is odd, the first half will have more elements than the second half.

        # Edge case check for small lists:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now that the list is split, we can reverse the second half.
        curr = slow.next
        slow.next = None

        pre = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        # Now we can begin the merge process.
        p1, p2 = head, pre
        while p2:
            t1, t2 = p1.next, p2.next
            p1.next = p2
            p2.next = t1
            p1, p2 = t1, t2
        






