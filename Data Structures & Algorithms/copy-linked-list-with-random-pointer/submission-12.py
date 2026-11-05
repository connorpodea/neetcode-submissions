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
        mapping = dict()

        # Loop through the original list. At each node, use the node as a key for the
        # dictionary, and store the new node as the value.
        trav = head
        while trav:
            mapping[trav] = Node(trav.val, None, None)
            trav = trav.next

        # After all of the nodes are created, we can assign the new nodes pointers to 
        # the other new nodes identified by the dict.

        trav = head
        while trav:
            og_node = trav
            new_node = mapping[trav]

            if og_node.next:
                new_node.next = mapping[og_node.next]
        
            if og_node.random:
                new_node.random = mapping[og_node.random]

            trav = trav.next

        return mapping[head] if head is not None else None