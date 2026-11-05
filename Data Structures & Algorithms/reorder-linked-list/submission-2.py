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
        # two pointers to recreate a list in the desired order.

        # If the list is empty or has only one node, no reordering is needed,
        # so we can return early to prevent any potential errors down the line.
        if not head or not head.next:
            return

        # To find the split point, we use slow and fast pointers, iterating until fast or fast.next is nil.
        # This positions our 'slow' pointer right at the end of the first half.
        # By doing this, the first half will naturally be equal to or one element longer than the second half.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now we isolate the second half by setting 'curr' to the node after 'slow', and then
        # we sever the link between the two halves so they become independent lists.
        curr = slow.next
        slow.next = None

        # Next, we reverse the second half.
        pre = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        # Now we can begin the merge process.
        # We set up two pointers at the heads of both lists and alternate linking them together.
        # Because the second half is guaranteed to be equal to or shorter than the first half,
        # the loop will terminate cleanly without crashing as soon as p2 runs out of nodes.
        p1, p2 = head, pre
        while p2:
            t1, t2 = p1.next, p2.next
            p1.next = p2
            p2.next = t1
            p1, p2 = t1, t2