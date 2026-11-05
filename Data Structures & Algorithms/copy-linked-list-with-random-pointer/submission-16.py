"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Early exit due to a base case where the list is empty
        if not head:
            return None

        # Loop through the original list. At each node, use the node as a key for the
        # dictionary, and store the new node as the value.
        mapping = dict()

        trav = head
        while trav:
            mapping[trav] = Node(trav.val)
            trav = trav.next

        # After all of the nodes are created, we can assign the new nodes pointers to 
        # the other new nodes identified by the dict.

        trav = head
        while trav:
            mapping[trav].next = mapping.get(trav.next)
            mapping[trav].random = mapping.get(trav.random)
            trav = trav.next

        return mapping[head]