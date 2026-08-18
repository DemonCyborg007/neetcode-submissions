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
        # Handle edge case for empty list
        if not head:
            return None
            
        # Dictionary to map old nodes to their corresponding new nodes
        old_to_new = {}
        
        # Pass 1: Create a clone of all nodes (without linking them yet)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Pass 2: Link the copied nodes' next and random pointers
        curr = head
        while curr:
            # If the original node has a next node, link the copied node's next
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            
            # If the original node has a random node, link the copied node's random
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
                
            curr = curr.next
            
        # Return the new head node using our mapping
        return old_to_new[head]

        